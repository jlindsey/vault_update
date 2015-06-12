import argparse
import json
import os
import sys
import tempfile
from subprocess import check_output, call, CalledProcessError


__vault_url__ = os.environ['VAULT_URL']


def parse_args():
    parser = argparse.ArgumentParser(description='Update an entry in Vault')
    parser.add_argument('key', metavar='KEY',
                        help='vault entry keypath (excluding the leading "secret/")')
    return parser.parse_args()


def main():
    args = parse_args()

    try:
        raw_val = check_output(['vault', 'read', '-address=%s' % __vault_url__,
                                '-format=json', 'secret/%s' % args.key])
    except CalledProcessError:
        print("ERR: Unable to read vault data")
        sys.exit(1)

    data = json.loads(raw_val)['data']

    temp = tempfile.NamedTemporaryFile(suffix='.json', delete=False)
    with temp.file as f:
        f.write(json.dumps(data, indent=2, separators=(',', ': ')))

    try:
        call([os.environ['EDITOR'], temp.name])
    except CalledProcessError:
        print("ERR: Unable to open your EDITOR")
        sys.exit(1)

    with open(temp.name, 'r') as f:
        try:
            data = json.loads(f.read())
        except ValueError as e:
            print("ERR: Unable to parse JSON")
            print(e.message)
            sys.exit(1)

    vault_args = ['vault', 'write', '-address=%s' % __vault_url__, 'secret/%s' % args.key]
    for key, val in data.iteritems():
        vault_args.append('%s=%s' % (key, val))

    try:
        call(vault_args)
    except CalledProcessError:
        print("ERR: Unable to write data back to Vault key")
        sys.exit(1)
