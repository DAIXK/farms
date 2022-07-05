# GENERATE and UPLOAD collection vaults

python3 generate_vaults_collection.py vaults_rdm_stc.json tokens_rdm_stc.json Gm3TfdTFJP5twZGfJFviLjQNP1YYgwRpLKVa1KXrujo8 RDM PARTNER_CONSTANT

./target/release/solana-farm-ctrl --keypair main_admin.json load --skip-existing Vault vaults_rdm_stc.json

./target/release/solana-farm-ctrl --keypair main_admin.json load --skip-existing Token tokens_rdm_stc.json

python3 init_vaults_collection.py Gm3TfdTFJP5twZGfJFviLjQNP1YYgwRpLKVa1KXrujo8 RDM SPT
