---
layout:     post
title:      Pixyll in Action
summary:    See what the different elements looks like. Your markdown has never looked better. I promise.
---

There is a significant amount of subtle, yet precisely calibrated, styling to ensure
that your content is emphasized while still looking aesthetically pleasing.

All links are easy to [locate and discern](#), yet don't detract from the [harmony
of a paragraph](#). The _same_ goes for italics and __bold__ elements. Even the the strikeout
works if <del>for some reason you need to update your post</del>. For consistency's sake,
<ins>The same goes for insertions</ins>, of course.

### Code, with syntax highlighting

Here's an example of some ruby code with line anchors.

{% highlight ruby lineanchors %}
# The most awesome of classes
class Awesome < ActiveRecord::Base
  include EvenMoreAwesome

  validates_presence_of :something
  validates :email, email_format: true

  def initialize(email, name = nil)
    self.email = email
    self.name = name
    self.favorite_number = 12
    puts 'created awesomeness'
  end

  def email_format
    email =~ /\S+@\S+\.\S+/
  end
end
{% endhighlight %}

Here's some CSS:

{% highlight css %}
.foobar {
  /* Named colors rule */
  color: tomato;
}
{% endhighlight %}

Here's some JavaScript:

{% highlight js %}
var isPresent = require('is-present')

module.exports = function doStuff(things) {
  if (isPresent(things)) {
    doOtherStuff(things)
  }
}
{% endhighlight %}

Here's some HTML:

{% highlight html %}
<div class="m0 p0 bg-blue white">
  <h3 class="h1">Hello, world!</h3>
</div>
{% endhighlight %}

And a bit of Swift code:

{% highlight swift %}

func superTest(name: String?) -> Bool {
  if let name = name {
    print(name)
    return false
  }
  return false
}


func showCounterLabels(message: String) {
  //
  // Important to set this state,
  // otherwise the remainingLabel will be updated with some other content
  //
  self.blockUpdateRemaining  = true
  self.remainingLabel?.alpha = 1
  self.counterLabel?.alpha   = 1
  self.hintLabel?.alpha      = 0
  self.remainingLabel?.text  = message
}

override func viewDidAppear(animated: Bool) {
  super.viewDidAppear(animated)

  let product = (self.reader == nil ? APIUser.Product.RandomCall : APIUser.Product.DedicatedCall)
  APIManager.getCostForProduct(product) { [weak self] (remaining: Int, pricePerUnit: Int, currentCoins: Int) in
    if (remaining <= 0) {
      self?.showNotEnoughCoinsAlert(isCall: true)
    } else if (currentCoins < ACConstants.CallThresholdLimit) {
      self?.showCallWarningCoinThreshold()
    } else {
      // call request
      self?.createCallRequest()
      // start seach animation
      ACCallSearchAnimation.startAnimationInView(self?.searchingImage)
    }
  }
}

{% endhighlight %}

# Headings!

They're responsive, and well-proportioned (in `padding`, `line-height`, `margin`, and `font-size`).
They also heavily rely on the awesome utility, [BASSCSS](http://www.basscss.com/).

##### They draw the perfect amount of attention

This allows your content to have the proper informational and contextual hierarchy. Yay.

### There are lists, too

  * Apples
  * Oranges
  * Potatoes
  * Milk

  1. Mow the lawn
  2. Feed the dog
  3. Dance

### Images look great, too

![desk](https://cloud.githubusercontent.com/assets/1424573/3378137/abac6d7c-fbe6-11e3-8e09-55745b6a8176.png)

_![desk](https://cloud.githubusercontent.com/assets/1424573/3378137/abac6d7c-fbe6-11e3-8e09-55745b6a8176.png)_


### There are also pretty colors

Also the result of [BASSCSS](http://www.basscss.com/), you can <span class="bg-dark-gray white">highlight</span> certain components
of a <span class="red">post</span> <span class="mid-gray">with</span> <span class="green">CSS</span> <span class="orange">classes</span>.

I don't recommend using blue, though. It looks like a <span class="blue">link</span>.

### Footnotes!

Markdown footnotes are supported, and they look great! Simply put e.g. `[^1]` where you want the footnote to appear,[^1] and then add
the reference at the end of your markdown.

### Stylish blockquotes included

You can use the markdown quote syntax, `>` for simple quotes.

> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse quis porta mauris.

However, you need to inject html if you'd like a citation footer. I will be working on a way to
hopefully sidestep this inconvenience.

<blockquote>
  <p>
    Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away.
  </p>
  <footer><cite title="Antoine de Saint-Exupéry">Antoine de Saint-Exupéry</cite></footer>
</blockquote>

### There's more being added all the time

Checkout the [Github repository](https://github.com/johnotander/pixyll) to request,
or add, features.

Happy writing.

---

[^1]: Important information that may distract from the main text can go in footnotes.


Indent using tabs equivalent to 4 spaces, and indent by inserting tab characters. Be sure to set xcode like this:

```
Indent using tabs equivalent to 4 spaces, and indent by inserting tab characters. Be sure to set xcode like this:
```


![_config.yml]({{ site.baseurl }}/images/screens/indentation.png)

Also think about automatically trim the whitespaces:

![_config.yml]({{ site.baseurl }}/images/screens/trim-whitespaces.png)

_![_config.yml]({{ site.baseurl }}/images/big.jpg)_

:+1:


:-1:



Hello.

C'est cool hein?

:+1: :+1: :+1: :+1: :+1: 

Pixyll is a simple, beautiful theme for Jekyll that emphasizes content rather than aesthetic fluff. It's mobile _first_, fluidly responsive, and delightfully lightweight.

It's pretty minimal, but leverages large type and drastic contrast to make a statement, on all devices.

<blockquote>
  <p>
    Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away.
  </p>
  <footer><cite title="Antoine de Saint-Exupéry">Antoine de Saint-Exupéry</cite></footer>
</blockquote>

## Where is it?

lol. everywhere.