const SlackBot = require('slackbots');
const fs = require('fs');

const dailyOffer = fs.readFileSync("daily-offer.json");
const botToken = 'xoxb-413082265606-412386441746-c58GEb3s2OqaSJFwEJzYjTgQ'


/**
 * Reads the json file containing the daily offer
 * 
 * @returns {JSON} jsonOffers - The offer in json format
 */
function getDailyOffer() {
  jsonOffers = JSON.parse(dailyOffer);
  return jsonOffers;
}

/**
 * Formats the offer and sends it to the channel
 */
function formatOfferToStringAndSend() {
  const dailyOffer = getDailyOffer();

  for (let item of dailyOffer.dailyOffer) {
    let finalString = '';
    finalString += `${item.name}, ${item.price}`;
    for (let offer of item.offers) {
      finalString += `\n  -${offer}`;
    }
    sendMessage(finalString);
  }
}

/** ----------------------------------------------------------------------------------
 * Slack bot
 *  ----------------------------------------------------------------------------------
 */

const bot = new SlackBot({
  token: botToken,
  name: 'prestobot'
});

bot.on('start', () => {
  sendMessage('Zdarek parek :smiley:');
});

bot.on('message', data => {
  if (data.type !== 'message') {
    return;
  }
  handleMessage(data.text);
  console.log(data);
});

/**
 * Decide wheter to reply to this message or not
 * 
 * @param {string} message - The whole message from user
 */
function handleMessage(message) {
  if (message.includes(' menu')) {
    formatOfferToStringAndSend();
  }
}

/**
 * Sends the message to general channel
 * 
 * @param {string} messageContent - The message to be sent 
 */
function sendMessage(messageContent) {
  const params = {
    icon_emoji: ':smiley:'
  };
  bot.postMessageToChannel('general', messageContent, params);
}