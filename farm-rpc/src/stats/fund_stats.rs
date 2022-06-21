use {
    log::info,
    serde::{Deserialize, Serialize},
    serde_json::to_string,
    solana_sdk::program_error::ProgramError,
};

#[allow(dead_code)]
pub const QUERY_LIMIT: u32 = 500;

#[derive(Serialize, Deserialize, Clone, Copy, Debug, PartialEq)]
pub enum Timeframe {
    Ticks,
    Hourly,
    Daily,
}

#[derive(Serialize, Deserialize, Clone, Copy, Debug, PartialEq)]
pub struct FundStatsRecord {
    pub timestamp: i64,
    pub assets_usd: f64,
    pub deposits_usd: f64,
    pub withdrawals_usd: f64,
}

pub struct FundStats {
    conn: i64,
}

impl std::fmt::Display for FundStatsRecord {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "{}", to_string(&self).unwrap())
    }
}
