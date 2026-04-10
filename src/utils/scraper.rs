use reqwest;
use std::{error::Error, fs};

pub async fn getcsv() -> Result<(), Box<dyn Error>> {
    
    // Future version make a function to scrape html for data. 
    // For site sources with html tables. #todo 
    // This link was forbridden when attmepted (https://www.ssa.gov/oact/STATS/table4c6.html)
    // Use this for future version (https://data.cdc.gov/National-Center-for-Health-Statistics/U-S-State-Life-Expectancy-by-Sex-2021/it4f-frdc/about_data)
     
    let url = "https://data.cdc.gov/api/views/w9j2-ggv5/rows.csv?";
    
    let data = reqwest::get(url)
        .await?
        .text()
        .await?;

    fs::write("file/raw/life_expectancy.csv", data)?;

    println!("✓ Data successfully saved to 'file/raw/life_expantancy.csv'");

    Ok(())
}