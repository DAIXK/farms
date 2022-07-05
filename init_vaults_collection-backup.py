#!/usr/bin/env python3

import subprocess
import json
import sys

# python3 generate_vaults.py vaults_rdm_stc.json tokens_rdm_stc.json Gm3TfdTFJP5twZGfJFviLjQNP1YYgwRpLKVa1KXrujo8 RDM SOLPATROL
def main():
    vault_program = sys.argv[1]
    protocol = sys.argv[2].upper()
    partner = sys.argv[3]

    p = subprocess.Popen('/Users/jabur/foton/solana-program-library/farms/target/release/solana-farm-client list-all farm',
                         shell=True,
                         stdout=subprocess.PIPE)
    data = '['
    for line in p.stdout.readlines():
        if line[:4].decode("utf-8") != protocol + '.':
            continue
        farm = line.decode("utf-8").split(':')[0]
        if len('VT.' + protocol + '.' + partner + '.' + farm[4:]) >= 32:
            raise ValueError("Len exceeded " + farm)
        p2 = subprocess.Popen('/Users/jabur/foton/solana-program-library/farms/target/release/solana-farm-ctrl vault-init ' +
                              protocol + '.' + partner + '.' + farm[4:] + ' 0',
                              shell=True,
                              stdout=subprocess.PIPE)
        if p2.wait() == 0:
            data += ','

    for line in p.stdout.readlines():
        if line[:4].decode("utf-8") != protocol + '.':
            continue
        farm = line.decode("utf-8").split(':')[0]
        if len('VT.' + protocol + '.' + partner + '.' + farm[4:]) >= 32:
            raise ValueError("Len exceeded " + farm)

        p3 = subprocess.Popen('/Users/jabur/foton/solana-program-library/farms/target/release/solana-farm-ctrl vault-enable-withdrawals ' +
                              protocol + '.' + partner + '.' + farm[4:],
                              shell=True,
                              stdout=subprocess.PIPE)

    for line in p.stdout.readlines():
        if line[:4].decode("utf-8") != protocol + '.':
            continue
        farm = line.decode("utf-8").split(':')[0]
        if len('VT.' + protocol + '.' + partner + '.' + farm[4:]) >= 32:
            raise ValueError("Len exceeded " + farm)
        p4 = subprocess.Popen('/Users/jabur/foton/solana-program-library/farms/target/release/solana-farm-ctrl vault-enable-deposits ' +
                              protocol + '.' + partner + '.' + farm[4:],
                              shell=True,
                              stdout=subprocess.PIPE)
        if p4.wait() == 0:
            data += ','

    for line in p.stdout.readlines():
        if line[:4].decode("utf-8") != protocol + '.':
            continue
        farm = line.decode("utf-8").split(':')[0]
        if len('VT.' + protocol + '.' + partner + '.' + farm[4:]) >= 32:
            raise ValueError("Len exceeded " + farm)
        p5 = subprocess.Popen('/Users/jabur/foton/solana-program-library/farms/target/release/solana-farm-ctrl vault-set-fee ' +
                              protocol + '.' + partner + '.' + farm[4:] + ' 6',
                              shell=True,
                              stdout=subprocess.PIPE)
        if p5.wait() == 0:
            data += ','

    for line in p.stdout.readlines():
        if line[:4].decode("utf-8") != protocol + '.':
            continue
        farm = line.decode("utf-8").split(':')[0]
        if len('VT.' + protocol + '.' + partner + '.' + farm[4:]) >= 32:
            raise ValueError("Len exceeded " + farm)
        p6 = subprocess.Popen('/Users/jabur/foton/solana-program-library/farms/target/release/solana-farm-ctrl vault-crank ' +
                              protocol + '.' + partner + '.' + farm[4:] + ' 1',
                              shell=True,
                              stdout=subprocess.PIPE)
        if p6.wait() == 0:
            data += ','


if __name__ == '__main__':
    main()