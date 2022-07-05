#!/usr/bin/env python3

import subprocess
import json
import sys


def main():
    vaults_out = open(sys.argv[1], 'w')
    tokens_out = open(sys.argv[2], 'w')
    vault_program = sys.argv[3]
    protocol = sys.argv[4].upper()
    partner = sys.argv[5]

    vaults = ["RDM.GKD.SOL-USDC-V5", "RDM.GKD.RAY-SOL-V3", "RDM.GKD.RAY-USDC-V3", "RDM.GKD.RAY-USDT-V3", "RDM.GKD.SOL-USDT-V5", "RDM.GKD.GENE-USDC-V5", "RDM.GKD.RAY-SRM-V5", "RDM.GKD.GENE-RAY-V5","RDM.GKD.ATLAS-USDC-V5","RDM.GKD.ETH-SOL-V5","RDM.GKD.SUSHI-USDC-V5","RDM.GKD.DFL-USDC-V5","RDM.GKD.ETH-USDC-V5","RDM.GKD.STSOL-USDC-V5","RDM.GKD.POLIS-RAY-V5"]

    data = '['
    for vault in vaults:
        p2 = subprocess.Popen('/Users/jabur/foton/solana-program-library/farms/target/release/solana-farm-ctrl generate Vault ' +
                              vault_program + ' ' + vault + ' VT.' + vault,
                              shell=True,
                              stdout=subprocess.PIPE)
        for log in p2.stdout.readlines():
            data += log.decode("utf-8").rstrip('\n')
        if p2.wait() == 0:
            data += ','

    data = data[:-1]
    data += ']'

    parsed = json.loads(data)
    vaults_out.write(
        '{"name": "Solana Vaults List", "timestamp": "2021-03-03T19:57:21+0000", "vaults":['
    )
    tokens_out.write(
        '{"name": "Solana Token List", "timestamp": "2021-03-03T19:57:21+0000", "tokens":['
    )
    first_token = True
    first_vault = True
    for obj in parsed:
        if 'chainId' in obj:
            if not first_token:
                tokens_out.write(',\n')
            else:
                first_token = False
            tokens_out.write(json.dumps(obj, indent=2, sort_keys=False))
        else:
            if not first_vault:
                vaults_out.write(',\n')
            else:
                first_vault = False
            vaults_out.write(json.dumps(obj, indent=2, sort_keys=False))

    vaults_out.write(']}')
    tokens_out.write(']}')
    vaults_out.close()
    tokens_out.close()


if __name__ == '__main__':
    main()