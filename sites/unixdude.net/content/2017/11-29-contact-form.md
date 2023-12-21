Title: How to build a Pelican contact form
Slug: pelican-contact-form
Category: Website
Tags: pelican, php
Date: 2017-11-29
Status: published

One of the first things I wanted to configure on this site was a contact form.  I searched and found that [Iain Houston documented how he configured one](https://iainhouston.com/blog/make-contact-form.html){:target="_blank"}.  I took his ideas and implemented my own slightly different version.

Where he used a separate template, I chose to use the base template and create a Pelican page for my contact form.

The contents of my `content/pages/contact.md` file are shown here.  This results in a page being created at `/pages/contact/index.html`, which I then added to MENUITEMS.

```
Title: Contact me
Slug: contact

<div class="col-md-12">
    <header class=jumbotron>
        <h1>Contact me</h1>
        <p>I'd love to hear from you.</p>
    </header>

    <form method="post" action="/php/submit.php">
        <div class="form-group col-md-6">
            <input type="text" class="form-control" id="name"  name="name" placeholder="Name" required>
        </div>
        <div class="form-group col-md-6">
            <input type="email" class="form-control validate email" id="email" name="email" placeholder="Enter email" required>
        </div>
        <p class="antispam">
            Leave this empty:
            <br />
            <input name="url" />
        </p>
        <div class="form-group col-md-12">
          <textarea class="form-control" rows="5" name="message" placeholder="Message" required></textarea>
        </div>
        <div class="form-group col-md-3 offset-md-3">
          <button type="submit" class="btn btn-primary">Submit</button>
        </div>
    </form>
</div>
```

The `content/php/submit.php` file is similarly simple:
```
<?php
if(isset($_POST['url']) && $_POST['url'] == ''){
    //The form was submitted
    $ouremail = 'your@email.com';
    // Important: if we add any form fields to the HTML,
    // and want them included in the email, we will need to add them here also
    $body = "This is the form that was just submitted:
    Name:  $_POST[name]
    E-Mail: $_POST[email]
    Message: $_POST[message]";
    // From:
    // Use the submitters email if they supplied one
    // (and it isn't trying to hack our form).
    // Otherwise send from our email address.
    if( $_POST['email'] && !preg_match( "/[\r\n]/", $_POST['email']) ) {
      $headers = "From: $_POST[email]";
    } else {
      $headers = "From: $ouremail";
    }

    // finally, send the message
    mail($ouremail, 'Contact Form submitted', $body, $headers );
    header('Location: /pages/thank-you/');
}
?>
```

You will also need a thank-you page.  Here's mine, saved as `content/pages/thankyou.md`:
```
Title: Thank you for contacting me
slug: thank-you

Your message has been sent.
```

Iain's script implements simple spam control.  To use it properly, you need to add some custom CSS so that the antispam field is hidden from view:
```
.antispam { display:none;}
```
