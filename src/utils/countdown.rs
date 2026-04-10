/*
use chrono::{DateTime, Utc, Duration};

pub struct TimeLeft {
    pub years: i64,
    pub days: i64,
}

impl TimeLeft {
    pub fn calculate_countdown(birthyear: i32) -> TimeLeft {
        let now = Utc::now();
        let duration = birthyear.signed_duration_since(now);
        
        TimeLeft {
            days: duration % 365,
            years: duration,
        }
    }
}

*/