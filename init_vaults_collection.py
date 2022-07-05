#!/usr/bin/env python3

import subprocess
import json
import sys

# python3 generate_vaults.py vaults_rdm_stc.json tokens_rdm_stc.json Gm3TfdTFJP5twZGfJFviLjQNP1YYgwRpLKVa1KXrujo8 RDM SOLPATROL
def main():
    vault_program = sys.argv[1]
    protocol = sys.argv[2].upper()
    partner = sys.argv[3]
    vaults = ["RDM.GKD.SOL-USDC-V5", "RDM.GKD.RAY-SOL-V3", "RDM.GKD.RAY-USDC-V3", "RDM.GKD.RAY-USDT-V3", "RDM.GKD.SOL-USDT-V5", "RDM.GKD.GENE-USDC-V5", "RDM.GKD.RAY-SRM-V5", "RDM.GKD.GENE-RAY-V5","RDM.GKD.ATLAS-USDC-V5","RDM.GKD.ETH-SOL-V5","RDM.GKD.SUSHI-USDC-V5","RDM.GKD.DFL-USDC-V5","RDM.GKD.ETH-USDC-V5","RDM.GKD.STSOL-USDC-V5","RDM.GKD.POLIS-RAY-V5"]

    data = '['
    for vault in vaults:
        p2 = subprocess.Popen('/Users/jabur/foton/solana-program-library/farms/target/release/solana-farm-ctrl vault-init ' +
                              vault + ' 0',
                              shell=True,
                              stdout=subprocess.PIPE)
        if p2.wait() == 0:
            data += ','

    for vault in vaults:

        p3 = subprocess.Popen('/Users/jabur/foton/solana-program-library/farms/target/release/solana-farm-ctrl vault-enable-withdrawals ' +
                              vault,
                              shell=True,
                              stdout=subprocess.PIPE)

    for vault in vaults:
        p4 = subprocess.Popen('/Users/jabur/foton/solana-program-library/farms/target/release/solana-farm-ctrl vault-enable-deposits ' +
                              vault,
                              shell=True,
                              stdout=subprocess.PIPE)
        if p4.wait() == 0:
            data += ','

    for vault in vaults:
        p5 = subprocess.Popen('/Users/jabur/foton/solana-program-library/farms/target/release/solana-farm-ctrl vault-set-fee ' +
                              vault + ' 6',
                              shell=True,
                              stdout=subprocess.PIPE)
        if p5.wait() == 0:
            data += ','

    for vault in vaults:
        p6 = subprocess.Popen('/Users/jabur/foton/solana-program-library/farms/target/release/solana-farm-ctrl vault-crank ' +
                              vault + ' 1',
                              shell=True,
                              stdout=subprocess.PIPE)
        if p6.wait() == 0:
            data += ','


if __name__ == '__main__':
    main()