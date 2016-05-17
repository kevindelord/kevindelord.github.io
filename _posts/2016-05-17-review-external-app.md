---
layout:     post
title:      How to review an iOS project
summary:    Ask yourself the right questions when it is about reviewing the complete code of an iOS app.
---

In the life of an iOS developer, the question of _'How good is this code'_ will come to you quite often.

When reviewing the code of an external app, you should ask yourself the right questions.

It is of course easier to judge someone else code than your own. But keep in mind that the project could have gone wrong at some point and its quality decreased quite significantly. There could be many different reasons: never satisfied customer(s), multiple change requests, time pressure, overly complicated design, too many different developers, etc. :cold_sweat:

This article lists many important points regarding the code quality but also the Xcode project and its setup. The answer of each question depends on what you and/or your company expects. But if you are able to answer those, then you should be able to explain to your Project Manager/CTO/Sales Manager how good or bad is the code.

## Repo Structure

- How is the repo structured ?
- Is it well ordered with logic subfolders or is it completely anarchic and random ?
- Is there a good and helpful `README` ?
- Where are the configuration files (`.plist`, `.yml`, `.json`) ?
- Is the `.xcasset` used? Only for the app icons or for all assets ?
- Are some submodules needed? Is it explained how and why ?

## Cocoapods & Podfile

- Is Cocoapods integrated ?
- Is it well integrated into each target ?
- How many libraries ?
- Are they versioned ?
- Are the libraries long deprecated ?

## Library

- How many hard coded libraries are set into the project ?
- Are they very deprecated ?
- Could they now been used as pods ?
- Are they _together_ in one `Libraries` (or `External`) folder or randomly put in the repository (in xcode and within the file system) ?

## Xcode Project

- Is it with or without Cocoapods ?
- Is it with or without Carthage ?
- How many targets ?
- If it's a workspace, are the targets shared ?
- Which architectures are configured ?
- How many build configuration per targets: Debug, Release, more ?
- Any weird and unexplained `Build Phases` ?
- Are all Cocoapods `Build Phases` set for all targets ?
- What about the Framework, Header and Library Search Paths, do they use `$(inherited)` ?
- What is the minimum deployment target ?
- Is this a universal app or a platform-dedicated app ?
- What is the Push Notification Provider ?
- Is there a storyboard? more than one ?
- Are all storyboards correctly used ?
- Is there a `Launch Screen` file ?
- Different app icons for each targets ?
- Is auto layout used ?
- How many independent interface files (`.xib`) are in the project ?

## Unit Tests

- Is there a unit test target ?
- Is it integrated into the project / build phases ?
- How many tests are written ?
- Are they good and relevant ?
- What is the code coverage value ?

## About the code

- Does it compile and run 'as is' ?
- Is there any warning ?
- Any kind of particularity in the API ?
- Do they use mock up data ? a fake-local backend for testing ?
- Are the URLs and API Endpoints hard-coded or not ?
- Do you see magic numbers ?
- Redondant code ?
- Static strings ?
- How much is the NSNotificationCenter used ?
- Is the displayed text localised ?
- Is the code documented, commented, explained ?
- Factory methods somewhere (that's a good thing) ?
- Any god objects (that's a bad thing) ?
- Does it contains ghost code from old iOS versions that are not supported anymore ?
- Does it contains ghost code from disabled/removed features ?
- Is there any functions longer than 40/60 lines ?
- Is there any duplicated logics ?
- How many undone TODOs ?
- Is there a constant file (that's a good thing) ?
- Is the appearance proxy used ?
- Is the code safe or quite buggy/crashy ?
- Swift: Is there a lot of optional unwrapping (usage of `!`) ?

## Data structure

- Is there a local database ?
- What kind of database: CoreData, MagicalRecord, Realm, Parse, etc. ?
- How is the data from the backend handled ?
- Does it work offline ?
- Is the code using hard-coded keys ?
- How many version of the data model exist ?
- Does it seems consistent and logic ?
- How many models are created/generated ?

## About the application

- Can you actually use the app, on simulator and on a device ?
- How is the design ?
- Does it look like an 2008 iPhone app that you will end up or not ?
- What is the feeling when you use the app ?
- Only webviews or native UI ?
- Is it slow ?
- How is the network handle (app automatically refreshing when network is turned back on/off) ?

## Conclusion

With all those questions you should now have a nice overview of the project.

Usually it is now time for you to write everything down and maybe estimate the costs of maintaining this code or starting the app from scratch.

You are the expert after all, your opinion matters !

Thanks for asking yourself those questions :stuck_out_tongue_winking_eye:
