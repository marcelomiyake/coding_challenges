// This stub file contains items that aren't used yet; feel free to remove this module attribute
// to enable stricter warnings.
#![allow(unused)]

pub fn production_rate_per_hour(speed: u8) -> f64 {
    match speed {
        1..=4 => return speed as f64 * 221_f64,
        5..=8 => return speed as f64 * 221_f64 * 0.9_f64,
        9..=10 => return speed as f64 * 221_f64 * 0.77_f64,
        _=> return 0_f64
    }
}

pub fn working_items_per_minute(speed: u8) -> u32 {
    (production_rate_per_hour(speed) / 60_f64) as u32
}
