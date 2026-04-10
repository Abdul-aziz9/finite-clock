use embedded_graphics::{
    mono_font::{ascii::FONT_10X20, MonoTextStyle},
    pixelcolor::BinaryColor,
    prelude::*,
    text::Text,
    primitives::{Rectangle, PrimitiveStyle},
    draw_target::DrawTarget,
};
use bmp_monochrome::Bmp;
use std::fs::File;
use std::io::Write;
use crate::engine::TimeDelta;
use crate::config::{DISPLAY_WIDTH, DISPLAY_HEIGHT};

pub fn generate_bmp(delta: &TimeDelta, output_path: &str) -> Result<(), Box<dyn std::error::Error>> {
    // 1. Create a buffer (1-bit color)
    let mut buffer = Bmp::new(DISPLAY_WIDTH, DISPLAY_HEIGHT)?;

    // 2. Define Styles
    let text_style = MonoTextStyle::new(&FONT_10X20, BinaryColor::On);
    
    // 3. Draw Content
    // Title
    Text::new("FINITE CLOCK", Point::new(320, 50), text_style)
        .draw(&mut buffer)?;

    // Big Number (Days)
    let days_str = format!("{} DAYS REMAINING", delta.days);
    Text::new(&days_str, Point::new(250, 240), text_style)
        .draw(&mut buffer)?;

    // Footer / Mission
    Text::new("MEMENTO MORI", Point::new(340, 400), text_style)
        .draw(&mut buffer)?;

    // 4. Save to Disk
    let mut file = File::create(output_path)?;
    buffer.write(&mut file)?;

    Ok(())
}