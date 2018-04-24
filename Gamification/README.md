## Gamification App
This is a side project of mine that will be using Gamification concepts for it's users to share knowledge, give feedback, log work and have fun while doing all this.

It is still miles away from being a real gamification app. For now it's only basic infrastructure.

More info (and hopefully more codes) coming soon.

### Features
* Work Report
* Mood Report
* Voluntary stuff report
* Vouching
* Feedback cycle
* Office Supplements
* Achievements

### Technical
I wanted to keep things simple and fun. I did not use a real web framework. App itself is AngularJs which talks to services writen in Python which are as pure as possible. And beyond services, there is the library in Pure Python as well.

##### Parts
* A web app built on AngularJs
* Python-Flask Services
* Library in Python
  * Guide : The API
  * Dungeon Master : Business Logic
  * Guard : Authentication
  * Dragoman : Multilingual Provider
  * Chronicler : Repo
* MongoDB
