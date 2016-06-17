---
layout: post
title: Configure an iOS build job on Jenkins
summary: See how to setup a new iOS build job on jenkins with automatic new releases and push to HockeyApp.
---

This page isn't about Jenkins and how it should be configured but more about iOS build jobs.

It explains how to setup a job in order to properly build and release a new version of your app on [HockeyApp](https://www.hockeyapp.net).

The most relevant fields are explained and detailed with screenshots.

## Naming

First of all, the name of the job should be very explicit. It should detail exactly _what_ it is and what it builds.

A good practice is to use the **target name** it is actually building.

More information about correct target naming on this article: [Xcode Project Configuration](http://kevindelord.io/2016/06/08/project-configuration/).

For example, with a project called `Dr.Oetker-Verlag` the build jobs on Jenkins would be named:

![_config.yml]({{ site.baseurl }}/images/jenkins/naming.png)

## SCM: Source Code Management

Jenkins allows you to pull and build project using different source code management such as [Git](https://git-scm.com), [Mercurial](https://www.mercurial-scm.org), etc.

In most case you need to specify two things:

- **Repository URL**: The url pointing to your source code.
- **Branch Specifier**: The branch to take the code from in order to build a new app version.

![_config.yml]({{ site.baseurl }}/images/jenkins/git.png)

## Build Triggers

There are multiple ways to automatically trigger a build process.

The most common ones are:

- `Build after other projects are built`

This will start a new build when another one has _successfully_ built.

- `Build periodically`

This will regurlarly trigger a new build at a constant interval of time.

- `Poll SCM`

This automatically build a new version every time something is pushed to the configured branch.

this option should only be activated for the base target, in most the `Project-Alpha-AdHoc`. If you need to build other jobs, do it manually.

![_config.yml]({{ site.baseurl }}/images/jenkins/poll_scm.png)

## Build Environment

The **resource to manage exclusion** avoid conflicts when building the same project with multiple targets at the same time.

All jobs for the same project should have the same value set.

If so, when scheduling 10 different builds they will all be done one by one.

![_config.yml]({{ site.baseurl }}/images/jenkins/resource.png)

## Build

### Critical block start-end and custom steps

In Jenkins it is possible to setup many different building phases: Android, iOS, Sonar Analysis, Custom shell scripts, etc.

In this article we are more interested in the following 2 build steps:

- Mobile: iOS Building
- Mobile: HockeyApp Deployment

But, whenever you need to add steps you should keep in mind to _always_ add them between a `Critical block start` and a `Critical block end`.

![_config.yml]({{ site.baseurl }}/images/jenkins/blocks.png)

To do so, use the button `Add build step`, select your step and drag'n'drop it between the critical blocks.

### Mobile: iOS Building

The _Mobile: iOS Building_ step contains 3 parts:

- Distribution Certificate
- Provisioning Profiles
- Build

#### Distribution Certificate and Provisioning Profiles

When you are trying to build jobs related to a target inside an Xcode project or workspace, be sure that the _Provisioning Profiles_ have been uploaded to Jenkins.

But also that the _Distribution Certificates_ that generated those profiles is correctly uploaded too!

![_config.yml]({{ site.baseurl }}/images/jenkins/certificate.jpg)

#### Build targets

The _build_ step lets you configure many different things such as the path to the project, the cocoapods integration, the target to build etc.

Here is a detailed list:

- `Project Folder`

The path to the folder containing your xcode project or workspace.

- `Run 'pod install'`

If enabled, execute the command line within the specified (or default) folder.

- `Target`

The target to build.

- `Scheme`

The **shared** scheme to build. This overrides the target.

If you setup your project as explained in the other topic, the `Target` and `Scheme` values should be the same than the `Product Name` within Xcode.

{% highlight swift lineanchors %}
PRODUCT_NAME = $(TARGET_NAME)
{% endhighlight lineanchors %}

- `Configuration`

The _build configuration_ used to build like `Debug` or `Release`.

- `Zip up dSYM`

Whenever the xcodebuild archives an app, it creates an `.ipa` file and one `.dSYM` file.

A `.dSYM` file stores the debug symbols for your app. It is later used to replace the symbols in the crash logs with the appropriate methods names. By doing so, the logs will be readable and will make sense for a normal person.

A zip version is required by HockeyApp and other crash reporter services.

- `Increment Build Number`

If enabled will increment the build number using the following command:

{% highlight swift lineanchors %}
$> agvtool next-version -all
{% endhighlight lineanchors %}

It should only be activated for the _base_ build job.

- `Push increment version`

If enabled will commit and push the changes made during the build to the selected branch.

It should only be activated for the _base_ build job.

##### Screenshot

The following screenshot shows the general rule about the build job configuration.
Please note that come configuration change if the target is the base one or not.

![_config.yml]({{ site.baseurl }}/images/jenkins/build.jpg)

##### Important

When building a whole new set of versions (`Alpha-AdHoc`, `Beta-InHouse`, etc.) always try to **just build the base job/target first**, and then (when it's done) all the others.

By doing so, you will make sure all new released versions will have the same version number.

### HockeyApp Deployment

The step to deploy to HockeyApp contains the following options:

- `API Token`

This token is given by HockeyApp and it gives you the permission to deploy new builds.

- `App ID`

The _App ID_ is actually the Hockey App ID for the current target. This unique identifier is generated when creating new app on Hockey.

To learn more about configuring HockeyApp, see [this topic](http://kevindelord.io/2016/04/19/configure-hockeyapp).

- `File to Deploy`

Path to the `.ipa` file to upload to Hockey.

- `Debug file`

Path to the `.dSYM.zip` files.

- `Release Notes`

Custom release notes.

- `Attach SCM changes to release notes`

If enabled, the commit messages will be used as release notes.

- `Make the build downloadable`

If enabled, the build will be downloadable from Hockey.

- `Private download page`

If enabled, only specific group (and registered) users will be able to access the download page.

- `Notify users`

If enabled, the users will be notified by email that a new version is available.

![_config.yml]({{ site.baseurl }}/images/jenkins/hockey.jpg)

PS: the tokens in the previous screenshot are fake.

Thanks for reading :smile:
