---
layout:     post
title:      Address Sanitizer
summary:    Xcode tool to find memory management issues.
---

When setting up a new project or when you want to actively debug a project the Address Sanitizer will help you to hunt down memory errors.
Xcode 7 can now build your app designed in a way to catch and debug memory corruption (stack and heap buffer overruns, use-after-free issues, etc.).
When these memory violations occur, your app can crash unpredictably or display odd behaviours.

## Integration

The Address Sanitizer is a very good tool to find memory management issues.
But at the same time, you need to rebuild the code and it slows down the app a bit (2x-5x CPU and 2x-3x memory).
Plus, to find errors you need to execute the code, thus only at runtime the memory corruption will be caught.
This tool only work on DEBUG and will never reach the customers/beta testers through an archived/RELEASE version.

To integrate it your projects, make sure to enable it where it make sense.
For example, by default on your UI and Unit tests but also on your ALPHA targets.
Unless they are drastically different, it does not make much more sense to enable it for BETA or LIVE targets.

## Configuration

To configure the Address Sanitizer for your a specific target, you need to **Edit the scheme** then:

- **Run** > Diagnostics > "Enable Address Sanitizer" checkbox
- **Test** > Diagnostics > "Enable Address Sanitizer" checkbox

![_config.yml]({{ site.baseurl }}/images/address_sanitizer/address_sanitizer.png)

Once done, go to the **Build Settings** of the same target and make sure that
The Optimisation Level is to **None [-O0]** in Debug. The configuration **Fast [-O1]** could also work but no higher optimisation would.

## Going further

If some errors persist and the Address Sanitizer does not help you to find the crashes, give a try to the other tools provided by Xcode.

- Enable Malloc Scribble
- Enable Malloc Guard Edges
- Enable Guard Malloc
- Enable Zombie Objects

![_config.yml]({{ site.baseurl }}/images/address_sanitizer/guard_malloc.png)

## Related articles

- [Use Your Loaf](http://useyourloaf.com/blog/using-the-address-sanitizer/)
- [WWDC 2015 Video](https://developer.apple.com/videos/play/wwdc2015/413/)
- [Xcode 7.0 release notes](https://developer.apple.com/library/ios/documentation/DeveloperTools/Conceptual/WhatsNewXcode/Articles/xcode_7_0.html)
