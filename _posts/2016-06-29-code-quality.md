---
layout: post
title: Code Quality in iOS
summary: Coding guidelines helping to write a better code in iOS
---

What are the different rules and code guidelines expected on an iOS project.

Depending on the language some following points might be useless or a even annoying for some developers.

But, when a developer keeps jumping between projects with different structures and languages without a global, strict (and restrictive) convention, the general quality will instantly decrease and slow down the development time.

In few words: the devs go crazy, all projects crash, end of the world, boom.


## Align & structure your code

Make sure the code is aligned to itself. This is just about structure and better looking code: the "=", the start of the lines, the function names, etc. The alignment is done with "tabulations".

It is also extremely appreciated to use comments to separate the class attributes and pragma mark between functions.

An example:

{% highlight swift %}
class MyViewController						: UIViewController {

	// MARK: - Outlets

	@IBOutlet var lettersGameButton			: UIButton?
	@IBOutlet var headBodyLegsGameButton	: UIButton?
	@IBOutlet var colorMatcherGameButton	: UIButton?

	// MARK: - Instance Variables

	var destinationType						: FFGameType?
	let transitionManager				 	= FFTransitionManager()

	// MARK: - View Lifecycle

	override func viewWillAppear(animated: Bool) {
	    super.viewWillAppear(animated)
		// Your code here.
	}

	// MARK: - Actions

	@IBAction func buttonPressed(sender: UIButton) {
		// Your code here.
	}
}
{% endhighlight %}

## No magic numbers

No magic numbers in any case, by any chance. It has to be or dynamic from an outlet, or calculated.

If, somehow, it is absolutely NOT possible, then create a constant in the constants file inside a structure.

The following example show how to create such structures.

The more your constants are *structured* the better.

PS: Note how everything is aligned.

{% highlight swift %}
//
// Constants.swift file
//
// MARK: - Games

struct GameConstants {

    // Informative comment about the type of constant
    static let ScrambleAnimationDelay	= 0.6

	// Animation Duration for pop up in [...]
	struct AnimationDuration {
	    static let FadeOut 				= 0.3
		static let FadeIn 				= 0.5
	}

 	// Top margin for view XY. Can't be dynamic because of [...]
    static let TopViewLeftMargin 		= 20
}
{% endhighlight %}

## No duplicated code

Duplicate code and/or logic are not allowed. In any case.
When coding you should always be able to reuse your code from the current app or common helpers.
The common excuses are : "it's just 3 lines" or "it's not important" or "but whatever".
All this just show how bad your code (structure) is. The debug of such code will be a nightmare for the developer in few months and a huge problem for the team.
Use libraries
In general we try to use open-source libraries as much as possible through cocoapods: AFNetworking, HockeySDK, DKDBManager, SwipeView, etc.
We also have other open libraries we use internally in all our projects:
Obj-C and Swift: DKHelper contains a whole bunch of helpers, categories and utilities.
Swift only: DKExtensionsSwift contains Swift extensions that can't be done in Obj-C and integrated into the DKHelper.

## NSNotificationCenter is hell

Try to avoid as much as possible the NSNotificationCenter. We have lost project due to this thing.
In few words, it sends magical calls to an unknown number of observers that do unknown actions without any flow/logic of what is actually going on in the app.
This very bad practice can seriously breaks the app and be the worst nightmare of your developer's life.
You should restructure again your code and use custom delegates or (even better) blocks instead.
PS: so far we just allow it for the keyboard notifications.

## KVO ain't good

Key Value Observing is mostly the same thing.
It is a bit too complex, not easy to read, and dangerous (could make the app crash if the observer or the observed objects are deleted).
In most cases delegates and blocks could be used instead!

## Constants in one single file

The constants should be in one single constants files called Constants.swift or Constants.h.
Of course this file should also be prefix depending on your project.
As said earlier, the more your file is structured the better. Create structures, add comments and pragma marks. Try to avoid single and anarchic constants without logic or explanation around.
In our case, what constant means is all string/number that are fixed and can't be dynamically changed.
They are used for database keys, API endpoint and response code, user default keys, segue identifier, etc. Actually all values that should not change. But if they do, they are all created in one single file and the change will take mostly 5 seconds.

Here is an example:

PS: Note how everything is aligned.

NOTE: Use the UpperCamelCase for all Enum, Struct, case, static variable names.

{% highlight swift %}
//
// User Default
//
enum HUUserDefault                          : String {

    // Keys set in PList files
    case AppId                              = "AppId"
    case HockeyId                           = "HockeyAppId"
    case APIBaseURL                         = "ApiBaseURL"
    case APIUserCredential                  = "ApiUserCredential"
    case APIPasswordCredential              = "ApiPasswordCredential"

    static let allValues                    = [AppId, HockeyId, APIBaseURL, APIUserCredential, APIPasswordCredential]
}


//
// Segues
//
enum HUSegueIdentifier                      : String {
    case FormulaDetail                      = "showDetailFormula"
    case SearchViewController               = "showSearchView"
}

//
// Cells
//
enum HUCellReuseIdentifier                  : String {
    case FormulaCell                        = "HUFormulaCell_id"
    case SearchCell                         = "HUSearchCell_id"
    case OptionCell                         = "HUOptionCell_id"
}

//
// Database
//
struct DB {

    static let DatabaseName                 = "Huethig.sqlite"

    struct Key {
        static let Id                       = "id"
        static let UpdatedAt                = "lastUpdate"
        static let Key                      = "key"
        static let Value                    = "value"
    }
}

//
// API
//
struct API {

    // Endpoints
    enum Endpoint                           : String {
        case Formula                        = "formula"
        case PDF                            = "pdf"
        case ProductId                      = "productid"
    }
}
{% endhighlight %}

## Defines also in a dedicated file

A define is a value used to configure and modify how the app reacts. They should be written in the Defines file.

In the end this file should be pretty small with just defines (Obj-C) or static variables (Swift) to really control the app:

- enable log or not.
- reset the database.
- unable the DEBUG mode for some libraries.
- disable a feature or not.

Here is an example in Swift:

{% highlight swift %}
//
// Debug
//
#if DEBUG
private let _isDebug = true
#else
private let _isDebug = false
#endif

//
// Configuration
//
struct Configuration {
	static let DebugAppirater			= (false && _isDebug)
	static let RestoreDatabase			= (false && _isDebug)
	static let EtagDisabled				= (false && _isDebug)
}

//
// Verbose
//
struct Verbose {


    // Manager and helpers
    struct Manager {
        static let API                  = false
        static let JSON                 = false
        static let DB                   = false
    }


    // Database model entities
    struct DB {
        static let Formula              = false
        static let Variant              = false
        static let Item                 = false
	}
}
{% endhighlight %}

## Control your log

There is nothing more annoying than starting an app and not being able to understand what is going on in the console as the log is flooding like an heavy rain.
To avoid that, we forbid to use anarchic NSLog or println lost in the code for no reason.
Usually we just use it to log dynamic errors as they are extremely important to know when/what/where something wrong happens.
But at the time, log is very helpful and can save a lot of time while coding/debugging. In this context, using logs is not a bad thing at all but should just be used and controlled wisely.
To do so use the  DKLog function. It takes as parameter a boolean to dynamically enable the log or not, and of course, a string to print.
The verbose boolean should be on the Defines header file.
Example:

{% highlight swift %}
DKLog(Verbose.Manager.API, "API Credentials ID: \(account) - password:\(password)")
{% endhighlight %}

## Comment your code
A beautiful code is also a documented code. You should always try to explain and document the logic your are implementing.
Even if it looks simple, and it surely does "now", for you but it won't in 5 months for another developer.
Comments above the functions are, of course, well appreciated to explain what they are doing, the purpose and general informations about them.
But inline comments are also very used to describe step-by-step what is going on inside the function.

{% highlight swift %}
/**
 Function to calculate top margin for the current view depending on [...]
 - parameter default: Default value used

 - return: CGFloat value corresponding to the calculated margin.
 */
func calculateTopMargin(default: Int) -> CGFloat {

	// Get the top x origin
	let separatorFrame = self.separator?.frame.x

	// Calculate position depending on [...]
	let finalPosition = (separatorFrame * 2) + self.defaultGap()

	// Apply frame
	self.popUpView?.frame = CGRectMake(...)
}
{% endhighlight %}

## Prefix files and classes

For historical reason we keep prefixing all our classes and files.
It might not be needed in Swift (due to the modules) but, as we sometimes work on an Obj-C project and one hour later on Swift, we should try to keep on having the logic.
For example with the following projects, we gave simple but efficient prefix: HH for Handhelp, DI for Digster, etc.

## Localise your project

How many times did you have to search though the whole project to fix a little typo? And then realise that this hard-coded string has been copy-pasted hundred times? How many times did you just do your app in one language and after months of development had to add a new language?
All this do happen... way too many times. It appears to be much better when the app is by default localised in whatever language with the Base localisation.
Even if the app is just in one language, you should always make the effort to add a key/value into a Localization.strings file.
Please, also note that even the localisation file is aligned.

{% highlight swift %}
"SETTINGS_MENU_SETTINGS"                = "Einstellungen";
"SETTINGS_MENU_RESTORE_PURCHASES"       = "Einkäufe wiederherstellen";

"NAVIGATION_TITLE_IMPRINT"              = "Impressum";
"NAVIGATION_TITLE_MENU"                 = "Menü";
"NAVIGATION_TITLE_PHOTO"                = "Rezeptbild";
"NAVIGATION_TITLE_PHOTO_LIST"           = "Rezeptbilder";
{% endhighlight %}

## No Storyboard localisation

If you decide to localise your storyboard you might save some times in the beginning as you can change the text for every label from dedicated string files.
This sounds very handy but it is actually a bad practice. The keys are not "developer-friendly" at all. They are just Stroyboard ids like 3ds-4e-drg, which is a nightmare to localise and translate as you don't know which label it is.
In general, force yourself to add a class to your labels and use the appearance framework or create an outlet and set the text dynamically.

### PhraseApp and Localisation services

For some projects you might want to integrate a string localisation service such as PhraseApp, Transiflex, LingoHub, etc.
They usually need/want just one strings file per language.  How could you do that with many strings file everywhere in your project?
Once again, just use one simple and single string file per language.

## PList configuration

On every project there is some third party libraries than need ID, client keys, project tokens, etc.
But there is also some constant values that are used by the app which are more than simple "constants".
I'm talking about external constant strings that need to be seen/found super easily and quickly.
For example backend/API URL, credentials, application name, etc.
As we configure our project with one plist file per target, it is then super easy to have different APIs for different targets.
Even better, in the code you do not need to change anything depending on your target or configuration.

![_config.yml]({{ site.baseurl }}/images/codequality/plist.png)

As you can see the keys are actually the ones defined in the Constants file. In the code it is now possible to fetch the value with just one simple line:

{% highlight swift %}
let applicationId = NSBundle.entryInPListForKey(UserDefault.ParseAppId.rawValue) as? String
{% endhighlight %}

## Function naming and convention

Be extremely careful on the function names: they have to be very explicit on what they do.
The other way around, the code should match the function name (the name should tell what the function does).
It is super easy to keep coding and changing your code, and in the end have a function doing something completely different than what its name says.

Other point, a function should not exceed 40 lines. This drastic limit forces the developer to think twice about the code and its structure.
A better encapsulation will help you with this rule.

## Images.xcassets

The Images.xcassets should be used as much as possible within the Resource folder.
Add all app icons, launch screens, image files, etc.
For vertical full screen size images you  can use the .xcassets as Launchscreen images.
But if your app as to deal with horizontal display you should use this library: UIImage+Autoresize

## Xib and Storyboard files

Small but important rule, do not commit unchanged xib files.
When you open one of them, Xcode always uselessly change some IDs, timestamp, version numbers, etc.
Please, discard those minor useless changes before committing. It is not extremely important but some conflicts could occurs and they are always annoying while reviewing the code.

## Database

This is not a tutorial on how to use/code with a database.
We usually use the library DKDBManager for our projects.
The point here is to remind you to never use hard coded keys, but always use the ones created in the constants file.
In the following example, two keys are used from the constant file:

{% highlight swift %}
override public class func primaryPredicateWithDictionary(dictionary: [NSObject:AnyObject]!) -> NSPredicate! {
    return NSPredicate(format: "\(DB.Key.Id) ==[c] \(GET_NUMBER(dictionary, JSON.Key.Id))")
}
{% endhighlight %}

## No Warning allowed

Another very important point are the compilation warnings. Without surprise we do not allow them at all.
A "small" warning today is a crash tomorrow. They are dangerous, exist for a reason and only show how lazy and inattentive a developer could be.
Be also extremely attentive when updating pods and other libraries. Warnings are also very helpful to understand what changes occurred and what needs to be done.

## Minor Optimisation

A good app is also about small optimisations all along the time of development.
One good thing to do is to use easy things for us that actually help a lot the processor at the runtime.
For example the division is a much harder task and a multiplication.

{% highlight swift %}
// Always prefer to use a multiplication instead of a division.
var a = 10 * 0.5

// Instead of
var b = 10 / 2
{% endhighlight %}

## Yes, rounded brackets!

Here we go with another restrictive rule: the rounded brackets. For historical reason and for a better readability a developer should use rounded brackets mostly everywhere.
It keep the code more understandable and prevent easy mistakes.
They are required when comparing values, ternary operators,  if else, while, ?? (swift) and where (swift).
Here you go with an example in Swift showing all cases:

{% highlight swift %}
var i = 0
var message : String? = nil
BOOL check = (true == false)  // comparison

while (check == true) {
	if (i >= 10) {  // if
		check = false
	} else if (i == 2) {
		i++
	}
	message = (check == true ? "valid" : "invalid") // ternary
	if let msg = message as? String where (i > 7) { // where
		println(message)
	}
	i++
}
return (message ?? "message does not exist") // ??
{% endhighlight %}

## Ternary operator


This ternary is amazing handful and pretty, but it can also be badly used and gives headaches to any developers.
One should only use it with just one level of operation and with rounded brackets.
Without those rules, a developer will code this:

{% highlight swift %}
value = a == b ? b != c ? 4 : d == e ? 6 : 1 : 0
{% endhighlight %}

This is horrible to read, debug and understand.

## Obj-C

Custom protocols (aka delegates)
Obj-C only: Create custom protocols (aka delegates) instead giving a pointer to a view controller. Example: a view controller containing a tableview. The cells should talk to the controller though a very specific delegate. The cell can of course receive data from the controller on the initialisation.
Modern Obj-C
Obj-C: use the "dot" logic because of modern-obj: self.songPositionLabel.text instead of [[self songPositionLabel] text]
Run the Modern Obj-C script once in a while.
Syntax
Here is a list of famous and well known Obj-C style guide:
https://github.com/NYTimes/objective-c-style-guide
https://github.com/raywenderlich/objective-c-style-guide
https://github.com/github/objective-c-style-guide

## Swift

As Swift tends to be the most used language in our company, a developer should follow this very specific style-guide:
https://github.com/kevindelord/swift-style-guide

It is based on other well known guidelines but has been improved to better match our goals and syntax.
The current page explains general setups and common knowledge when developing an app.
It is as much important as the swift-style-guide page.