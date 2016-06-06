---
layout: post
title: Provisioning Profiles
summary: How to manually update provisioning profiles on your local machine and on your project when you do not trust Xcode's black magic.
---

Once in a while you suddenly need to create or update a whole bunch of provisioning profiles as a new device needs an alpha or beta version.
This detailed tutorial explains how to properly remove old provisioning profiles and install fresh new ones.

## Adding a device

To make sure you can develop or install an AdHoc release on a specific device, this device UDID needs to be included within a provisioning profile.
To do so you need the following information:

- Valid UUID (with iTunes)
- Owner name's
- Owner company's
- Device type: iPhone/iPad 6(S)(Plus)
- Device Color: black, grey, white, gold, etc.

Then to register the device, go to the Apple Developer Portal and specify the new device name like this: "Company Name Type Color"

Examples:

- `SMF Ruediger iPhone 6s Black`
- `Adviqo Andreas iPhone 5s White`

When creating the new provisioning profiles, make sure that this new device is selected.

On the developer portal, select and update manually one by one all profiles you need (`DEBUG` and/or `RELEASE`).

Reminder: You don't need to update the InHouse-Release profiles as they are NOT linked to a specific list of devices.

## Create a new provisioning profile

### Naming Convention

The name of every single provisioning profile is very important and must be as explicit as possible.

It should follow the [same convention](TODO :cat:) than the target's in Xcode.

In few words, the name of the (pro)file should contains every single information:

- The project.
- The target.
- The type of distribution.
- The build configuration (see below).

### Build configuration: which type of profile

Whenever you create or update a profile, you should ask yourself what kind of profile to want.

Is it to develop and debug the project on a device or to install it through Hockey and/or TestFlight on many devices?

Depending on your needs, the final name of the profile should have one of the following suffix:

- `DEBUG` if you want to develop on it.
- `RELEASE` it is just for beta testing (project managers, customers, etc.)

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

Using the finder and by mouse-clicking :

- Remove all provisioning profiles from your download folder.
- Download ALL profiles (even the debug ones) but do NOT open them.

### b. Remove old profiles

Remove all provisioning profiles used by xcode for the current project by using the bundle identifier.

:warning: Of course only remove the profiles that you want to update. :warning:

On the terminal:

{% highlight swift lineanchors %}
$> cd ~/Library/MobileDevice/Provisioning\ Profiles
$> rm -v `grep -l "com.smartmobilefactory.adviqo.blabablabl" *`
{% endhighlight lineanchors %}

### c. Install new profiles

Then when you are done removing all old/deprecated profiles, you can install the new ones.
To do so just open them in the finder (select all and double click).

### d. Set new profiles in Xcode ( + git )

Then you will need the terminal to do the following (select current project and git branch ):

1. Go inside your current project's directory:

{% highlight swift lineanchors %}
$> cd ~/Projects/MyAwesomeApp/
{% endhighlight lineanchors %}

2. Create a new branch if needed or just make sure the current one is up to date!

{% highlight swift lineanchors %}
$> git pull origin YOUR_BRANCH // <- update the current branch
$> git checkout -b "update_profiles" // <- create a new branch
{% endhighlight lineanchors %}

Open the workspace, check all targets and **set the new provisioning profiles** instead of the invalid ones.

An invalid provisioning profile appears as hash (`7894212c-6d54-4fec-baa9-a2441fb613c4`) instead of a real and valid name.

Finally push your changes:

Check that you just changed the provisioning profiles

{% highlight swift lineanchors %}
$> git diff
{% endhighlight lineanchors %}

2. Git push on your branch

{% highlight swift lineanchors %}
$> git add .
$> git commit -m "Update Provisioning Profiles"
$> git push origin YOU_BRANCH
{% endhighlight lineanchors %}

3. Create a Pull Request on Github !

## Try it out !

If you successfully arrived to this point, just try to build the build jobs and release new versions :blush:
