---
layout: post
title: Xcode Project Configuration
summary: How to configure a new Xcode project and ready to code!
---

This page present one way to configure the structure of a repositoy containing an Xcode project.

It intends to set a clear and easy file hierarchy and configuration.

Within Xcode the targets are used to differentiate the builds and the _configuration_ stays untouched.

## Project structure

Your project's repository should be structured like this:

| Folder  | Description |
|:------|:------------|
| Core |	All our own code and header files (structured with subfolders): AppDelegate, Defines.h, Constants.h, ViewController/Dashboard, AdditionalViews/Cell/..., etc. |
| Resources |	Everything that isn't code and can be exchanged easily by anybody: Images(.xcassets), Settings.Bundle, HTML, Localisation string files, etc. |
| External | Third Party libraries that cannot be integrated with as pod. |
| Helpers |	Helper and manager classes that are generic enough to be copied/pasted (and slightly modified) into projects: HockeySDK, APIManager, DBManager, etc. |
| Podfile |	https://cocoapods.org/ |
| Podfile.lock |	https://cocoapods.org/ |
| Cartfile | |
| Cartfile.resolved | |
| Pods |	Folder containing pods code sources. Should not be pushed on the repo. (Update the gitignore file!). |
| PLists |	Folder containing all target info plist and CloudKit entitlements files: Dr.Oetker-Verlag-Alpha-AdHoc-Info.plist, Digster Live.entitlements. |
| README |	File explaining, at least, how to clone, configure (submodules + pods) and run the project. |
| Submodules | All submodules (sub repositories) for external libraries or small helpers. |
| xcodeproj |	The Xcode project file. |
| xcworkspace |	The Xcode workspace (current project + pods integrated). |
| .gitignore |	Determine which files and directories to ignore in git, more information below. |
| .swiftlint.yml |	Integrate and configure Swiftlint. See the dedicated page for more information. |

## Schemes and Targets

The targets should be used to differentiate your builds. In few words there should be one target per version and per certificate type (`Alpha`, `Beta`, `AdHoc`, `InHouse`, etc.).

Indeed, it could get a bit annoying to have so many targets for a single app but...

As each target posses one PList file, it becomes then much more easier to configure the backend/API URL, the 3rd party keys (_[HockeyApp](https://www.hockeyapp.net)_, _[Parse](http://parse.com)_, _[Google Analytics](http://www.google.com/analytics)_, etc.) or any other custom attributes.

Plus, within Xcode, anybody could easily see and understand the different versions available.

The only used _build configurations_ are: `Debug` and `Release` and in no case `AppStore` or `AdHoc`. Those are two very different things!

### Target naming convention

First and more important the naming convention around the targets. For the example, let us take a look at the _Dr.Oetker_ project.

![_config.yml]({{ site.baseurl }}/images/project_config/targets.png)

What does `Dr.Oetker-Verlag-Alpha-AdHoc` mean?

- `Dr.Oetker-Verlag`: the project name.
- `Alpha`: the target type.
- `AdHoc`: the apple certificate type.

All those names are separated by `"-"`, no whitespace allowed.

#### Target Explanation

Unless the project needs very different targets, in most case it has 3 targets:

- `ALPHA`: for the main development and daily releases for the developers. The dev environment for the API should be used.
- `BETA`: weekly release for the beta testers and project managers. The staging environment for the API should be used.
- `LIVE`: special release using the distribution certificate and AppStore provisioning profiles. The live environment for the API should be used.

#### AdHoc / InHouse / AppStore

To develop on iOS/OSX a developer needs to have a valid Apple developer account.

Two kind of account are provided by Apple:

- The **developer account** where people can submit an app to the store and use _In-App-Purchases_. The devices allowed to install the app are controlled and limited (provisioning profiles).
- The **enterprise account** where people can **NOT** submit an app but distribute it to any device with a single download link (through [HockeyApp](https://www.hockeyapp.net) or [TestFlight](https://developer.apple.com/testflight/) for example).

##### `AdHoc`

In our current example _Dr.Oetker_; the app needs In-App-Purchases. One distribution certificate created from the developer account should be used.

The target should contains the word `AdHoc`.

##### `InHouse`

But to simplify the distribution and the testing we should provide a full version without IAP where everything is already bought.

For this case we can use _enterprise account_ and an `InHouse` target. This target is mainly use for the testing, the press releases, etc.

##### `AppStore`

Finally, `AppStore` represents a target with a very specific provisioning profile. This kind of profile let a build be submitted on the store but can't be installed on device using Xcode nor distributed through Hockey.

#### DEBUG / RELEASE

The terms `DEBUG` and `RELEASE` should strictly be only used for the build configurations.

Do not use them on the targets of schemes names.

They should actually be use on the provisioning profile names. Example with a project called "_AESD_":

![_config.yml]({{ site.baseurl }}/images/project_config/code_sign.png)

:warning: The provisioning profile file name should match the target and scheme name.

### Scheme

The name of the scheme is also important. It should be the very same one than the target it is related to.

There should be one scheme per target and none per configuration and sorted following this priority order:

1. `ALPHA`
2. `BETA`
3. `LIVE`

And then by

1. `AdHoc`
2. `InHouse`
3. `AppStore`

![_config.yml]({{ site.baseurl }}/images/project_config/shared_targets.png)

PS: For the sake of Jenkins they have to be _shared_ (see the tick bock above).

Within Xcode, If you want to build on `Release` and not in `Debug` then edit the scheme and build again (don't forget to set the configuration back).

## Build Settings

The Build Settings are independant for every target. They should be correctly setup and maintained.

### Content contains Swift code

If your code is in Swift or contains Swift code you need to specify it in the **Build Settings**.
If you forget this step, the build will be rejected by iTunesConnect.

![_config.yml]({{ site.baseurl }}/images/project_config/embedded_swift.png)

Note: this is now the default behaviour within Xcode, it is nonetheless good to double check before submitting.

### Versioning

The versioning is used in every project to differentiate released builds. The Continuous Integration process increment the build number for every new release.

On Jenkins, it executes the following command line:

{% highlight swift lineanchors %}
$> agvtool next-version -all
{% endhighlight lineanchors %}

In the build settings, do not forget to set the **Current Project Version** to 1 manually. Later on, your CI should update that value manually.

![_config.yml]({{ site.baseurl }}/images/project_config/versioning.png)

### Configuration Files

For each target, the configuration files such as **Prefix.pch**, **Info.plist** or the **bridging-header.h** should be set without the `$(SRCROOT)` prefix.

This prefix isn't required by the compilation process and actually fails the versioning process (explained previously).

For example, in the build settings for the PList file:

![_config.yml]({{ site.baseurl }}/images/project_config/info-plist.jpg)

### Product Name

In order to get a correct build process on Jenkins the **Product Name** also should be correctly setup.

The value for each target has to be `$(TARGET_NAME)`:

![_config.yml]({{ site.baseurl }}/images/project_config/product-name.jpg)

### Custom Flags

Finally, one very handy point is to correctly set for each target some compilation flags.

Those flags can be used in the code to differentiate the `ALPHA` version from the `BETA` or between `AdHoc` and `InHouse`.

In Swift, the **Other Swift Flag** should be set as shown:

OTHER_SWIFT_FLAGS`

![_config.yml]({{ site.baseurl }}/images/project_config/flags.png)

In Objective-C, the **Preprocessor Macros** should be set like this:

`GCC_PREPROCESSOR_DEFINITIONS`

![_config.yml]({{ site.baseurl }}/images/project_config/macros.jpg)

:warning: Do not forget to add the `$(inherited)` flag!

### Bitcode

The Bitcode[^1] should be enabled by default for all targets of all project.

Problem, if you are using (old) static libraries this optimisation has not been done when compiled.

Which means that your app can not have the Bitcode enabled as one (small) part of it hasn't.

![_config.yml]({{ site.baseurl }}/images/project_config/bitcode.png)

#### Suggestion

Always enable the Bitcode for your project, then search for static libraries (`.a`) in your project and in the Pods.
Try to understand how old they are and if they include this optimisation or not.
For example the latest versions of the [FlurrySDK](http://developer.yahoo.com/flurry) or [GoogleAnalytics](https://developers.google.com/analytics/devguides/collection/ios/v3/) do, but the old deprecated ones don't.

## Gitignore

Within an iOS project many files are either redundant or private or even useless for a git repository.
When you configure a new project, make sure to add and commit a 'git ignore' file at the root of the repo.

Of course, name the file `.gitignore`.

A good practice is to use the ones made by Github:

- Swift

{% highlight lineanchors %}
$> curl https://raw.githubusercontent.com/github/gitignore/master/Swift.gitignore > .gitignore
{% endhighlight lineanchors %}

- Objective-C

{% highlight lineanchors %}
$> curl https://raw.githubusercontent.com/github/gitignore/master/Objective-C.gitignore > .gitignore
{% endhighlight lineanchors %}

#### Update existing `gitignore`

If you add or update this file later in the development of the project, some files might have already been pushed to the server.

To remove those useless and/or deprecated files, add or update the **.gitignore** file and enter the following in the command line:

{% highlight swift lineanchors %}
$> git add .gitignore
$> git commit -m "Update gitignore file"
$> git rm -r --cached .
$> git add .
$> git status
{% endhighlight lineanchors %}

If you now see some files marked as deleted, commit and push the changes to the server !

{% highlight swift lineanchors %}
$> git commit -m "Remove ignored files"
$> git push
{% endhighlight lineanchors %}

## Conclusion

In this article we have seen how to structure the repository, configure one target per version of the app and some naming conventions.

The important parts of the build settings have been explained and the git ignore detailed.

Of course, not all of those points might suit your projects but could help you finding some problems!

Thanks for reading :kissing_heart:

---

[^1]: **Bitcode**: When you archive for submission to the App Store, Xcode compiles your app into an intermediate representation. The App Store then compiles the bitcode down into the 64- or 32-bit executables as necessary. [Xcode Release notes](https://developer.apple.com/library/ios/documentation/DeveloperTools/Conceptual/WhatsNewXcode/Articles/xcode_7_0.html#//apple_ref/doc/uid/TP40015242-SW5)
