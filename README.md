# splatnetter
Splatnetter is a tiny script that queries the last tweet of a twitter bot that publishes items currently in the SplatNet store and will send a text message to the recipient if it fits the criteria.

It was written to be hosted on AWS Lambda and has a build script that you can run that will create the zip file that you upload to AWS. 


## How To Use
It's pretty straightforward. The script is basically a one shot, just make sure you have the proper environment variables set and everything will work fine.

Note: You will need a Twitter App registered and a Twilio account to get the proper API keys for everything to run smoothly. I include dotenv already so you can just put those in a .env file locally but I'd recommend using the built in environment variable functionality on AWS if you are going to use this.
