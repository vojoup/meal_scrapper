const fs = require('fs');
const dailyOffer = fs.readFileSync("daily-offer.json");

jsonOffers = JSON.parse(dailyOffer);

for (let item of jsonOffers.dailyOffer) {
  console.log(`${item.name}, ${item.price}`);
  for (let offer of item.offers) {
    console.log(`  -${offer}`);
  }
  console.log();
}