# Twitter Tweets
<p>A simple web app that scrapes the Twitter API and display the most recent tweets for a @Twitter username that is searched.</p>
<p>Frontend built with **AngularJS** and **Semantic UI**. Backend built with **Python** and **Tweepy**.</p>

## See the Live Demo
See a live demo at [http://35.196.93.111/twittertweets](http://35.196.93.111/twittertweets/)
<p align="left">
  <a href="http://35.196.93.111/twittertweets/">
    <img src="./images/twitter_app1.png" alt="Screenshot of App">
    <img src="./images/twitter_app2.png" alt="Screenshot of App Search">
  </a>
</p>

## Launching the App Locally
*Follow the instructions in the [./backend](./backend) folder to set up a backend API.*
*You will need to launch the Python backend API for the search functionality to work.*
<br><br>
The *frontend* portion of the application can be launched by following these steps...

### Prerequisites
* [NodeJS](https://nodejs.org/en/download/) - an open source server framework
* [npm](https://www.npmjs.com/get-npm) - a package manager for Node.js packages
* [http-server](https://www.npmjs.com/package/http-server) - a simple, zero-configuration command-line HTTP server
* [Python](https://www.python.org/downloads/) - for an alternative server (optional)

### Installing
Clone this repository onto your local computer
```
git clone -b master https://github.com/johnkntran/twitter-tweets.git twitter-tweets
```
Then `cd twitter-tweets` to go into the repository.
Install all package dependencies
```
npm install
```
Run a local HTTP server, such as *http-server*
```
http-server
```
Alternatively, if you have Python installed, you can run a simple HTTP server
```
python -m SimpleHTTPServer 8080
```
Navigate to [http://localhost:8080/](http://localhost:8080/) on your browser and you should see the application running.
