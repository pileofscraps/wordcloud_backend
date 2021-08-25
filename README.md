Offchain Dynatic NFT Generation
============

While dApps on Ethereum have grown in complexity, depth, and breadth in the past few years. One missing piece is the efficient querying of blockchain information in real-time.

Users need to know immediately when their trades execute, when their transactions fail, when their auction bid has been accepted, or when a wallet of interest has aped into some new token. Without these notifications, trades can be missed, critical actions are forgotten, and ultimately users end up abandoning your dApp. 
Unfortunately, building these real-time notifications into your dApp has traditionally been complicated, time-consuming, and error-prone. But now with Alchemy Notify, sending real-time push notifications to your users for critical events such as dropped transactions, mined transactions, wallet activity, and even gas price changes is straightforward, easy, and dependable. 

In this tutorial, we’ll look at an example of how, with just a few lines of code, you can build a Dynamic NFT with the 🔋 power of Alchemy Notify.

***
For ease of user experience, this particular tutorial to run on Heroku, but you are more than welcome to use other service providers!
***

### Problem Statement: ###

Wanting to create a dynamic off-chain NFT that adjusts it's image based on chain interations, we use Alchemy's Enhanced API method (particularly Alchemy Notify) specifically to get the Address Activity notifications.  This lets us hook onto any transactions that interact with our target address and allows us to inject that info into our SVG generation. To generatively create our NFT, we use the python package `wordcloud` to create a wordcloud of all the addresses that have interacted with our NFT.  

To summarize, our Heroku server is configured to accept address notifications, add addresses to our wordcloud, and return an updated NFT SVG based on on-chain interacions!

Note: This serves as an adjunct component to the NFT's minting which takes place via Scaffold-ETH!  If you want to do this without Scaffold-ETH, you simply need to point the tokenURI towards the Heroku link generated via the steps below!

### 🚀 Launching with Heroku ###

 1. Get the repo!

      * `https://github.com/pileofscraps/wordcloud_backend.git`

For all Heroku dependent documentation, refer to:
https://devcenter.heroku.com/articles/getting-started-with-nodejs?singlepage=true 
for more detailed instructions.  The Heroku instructions included below are abridged.

 2. Install Heroku-CLI and verify/install dependencies.

      * Download Heroku-CLI based on your OS [https://devcenter.heroku.com/articles/heroku-cli]
      * After installation, open your terminal and run `heroku login`; follow the commands that follow to login to your Heroku account.  If you don't have a Heroku account, you can [sign up for one](https://dashboard.heroku.com/apps)!
      * Run `node --version`.  You may have any version of Node greater than 10.  If you don’t have it or have an older version, install a more recent version of Node.
      * Run `npm --version`.  `npm` is installed with Node, so check that it’s there. If you don’t have it, install a more recent version of Node:
      * Run `git --version`   Check to make sure you have git installed.  

 3. Initiate Heroku.
 
      * Run `heroku create` to create your heroku app. Take note of the info that pops up in the terminal, especially the URL that looks like  http://xxxxxxxxx.herokuapp.com/ That's the URL for your dashboard!

 4. Deploy Heroku.

      * Run `git add .`
      * Run `git commit -m "added Alchemy keys"`
      * Run `git push heroku master` to push and deploy your heroku app.
     
🎉 Congratulations on your dApp deployment! Feel free to edit this NFT, change its behavior, or make the backend more robust!

NOTE: Heroku will automatically sleep apps after a set period of time so you will need to make sure you app is up and awake for unchain acitivity to be recognized!  
