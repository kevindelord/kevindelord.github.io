---
layout: post
title: Provisioning Profiles
summary: How to manually update provisioning profiles on your local machine and on your project when you do not trust Xcode's black magic.
---

Once in a while you suddenly need to create or update a whole bunch of provisioning profiles as a new device needs an alpha or beta version.

The usual process is to open the Apple developer portal, update the provisioning profiles and set them into your project.

For this last step you could theoretically use Xcode's black magic. But if like me, you do not _trust_ it, a manual approach could be more interesting.

This detailed tutorial explains how to properly and manually remove old provisioning profiles and install fresh new ones.

## Adding a device

To make sure you can develop or install an `AdHoc` build release on a specific device, this device's UDID needs to be included within a provisioning profile.

To do so you need the following information:

- Valid UDID (with iTunes)
- Owner name's
- Owner company's
- Device type: iPhone/iPad 6(S)(Plus)
- Device Color: black, grey, white, gold, etc.

Then to register the device, go to the Apple Developer Portal and specify the new device name like this: "`Company Name Type Color`"

Examples:

- `SMF Ruediger iPhone 6s Black`
- `Adviqo Andreas iPhone 5s White`

When creating the new provisioning profile, make sure that this new device is selected.

On the developer portal, select and update manually one by one all profiles you need (`DEBUG` and/or `RELEASE`).

Reminder: You don't need to update the `InHouse-Release` profiles as they are NOT linked to a specific list of devices.

## Create a new provisioning profile

### Naming Convention

The name of every single provisioning profile is very important and must be as explicit as possible.

It should follow the same convention than the target names in Xcode.

In few words, the name of the (pro)file should contains every information such as:

- The project name
- The target name
- The type of distribution
- The build configuration (see below)

### Build configuration: which type of profile

Whenever you create or update a profile, you should ask yourself what kind of profile you want.

Is it to develop and debug the project on a device or to install it through [HockeyApp](https://hockeyapp.net) or [TestFlight](https://developer.apple.com/testflight/) on many devices?

Depending on your needs, the final name of the profile should have one of the following suffix:

- `DEBUG` if you want to develop on it.
- `RELEASE` if it is just for beta testing (QA, project managers, customers, etc.)

### Examples

Here is a list of valid provisioning profile names:

- `AESD Alpha InHouse DEBUG`
- `AESD Alpha InHouse RELEASE`
- `AdviqoReader Live Testing InHouse RELEASE`
- `Catalyst42 GFR Beta InHouse DEBUG`
- `Pons SPK FR Beta InHouse RELEASE`
- `Pons SPK EN Beta AdHoc RELEASE`
- `Pons SPK EN Alpha AdHoc DEBUG`


## Update the Xcode project

### a. Refresh local profiles

Using the finder and your favourite web browser:

- **Remove** all provisioning profiles from your download folder.
- For a specific project, **download all** profiles (even the debug ones) but do NOT open them.

### b. Remove old profiles

Now it is time to remove all provisioning profiles used by xcode for the current project.

Use the bundle identifier to select the right profiles / target.

:warning: Of course only remove the profiles that you want to update. :warning:

On the terminal:

{% highlight swift lineanchors %}
$> cd ~/Library/MobileDevice/Provisioning\ Profiles
$> rm -v `grep -l "com.your.awesome.bundle.identifier" *`
{% endhighlight lineanchors %}

### c. Install new profiles

Then when you are done removing all old/deprecated profiles, you can install the new ones you downloaded few minutes ago.

To do so just open them from the finder (select and double click).

### d. Set new profiles in Xcode ( + git :octocat: )

Before changing the Xcode configuration, create a new git branch (it is _always_ better to work on new branches):

{% highlight swift lineanchors %}
$> git pull origin YOUR_BRANCH // <- update the current branch
$> git checkout -b "update_profiles" // <- create a new branch
{% endhighlight lineanchors %}

Then open the workspace and check the targets.

An invalid provisioning profile appears as hash (`7894212c-6d54-4fec-baa9-a2441fb613c4`) instead of a real and valid name.

That means that the corresponding profile is not on your computer. Which is good! That very one was old and is now deprecated.

Click on the hash and **set the new provisioning profiles** instead.

In case you have a long list of profiles, the latest installed are always at the top.

To check that you just correctly changed the provisioning profiles, use git and your new branch:

{% highlight swift lineanchors %}
$> git diff
{% endhighlight lineanchors %}

Finally, push it all to the server and create a Pull Request !

{% highlight swift lineanchors %}
$> git add .
$> git commit -m "Update Provisioning Profiles"
$> git push origin YOU_BRANCH
{% endhighlight lineanchors %}

## Try it out !

If you successfully arrived to this point, just try to build and release new versions :blush:
