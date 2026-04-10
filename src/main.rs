mod utils;
use std::error::Error;
use tokio;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>>{

    utils::scraper::getcsv().await?;

   Ok(())

}