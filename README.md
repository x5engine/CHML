# CHML is the new HTML




CHML is a proposed syntax for writing HTML (HyperText Markup Language), which is a markup language used for structuring and formatting content on the web. CHML uses a different syntax and conventions than standard HTML, and it is not a widely-used or recognized language. In CHML, elements are defined using keywords, such as div or p, and attributes, such as id or class, are defined using special syntax, such as #id or .class. The content of an element is defined between the : and /: delimiters.

## A new take on HTML that makes it easier and faster to write and read

It can be used in React or other libraries...

Here is an example of how a CHML code snippet could be written:

```
div#app.container:
  h1#heading.primary-heading:Welcome to our website/:
  p#intro-text.lead:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidat
```

Here is a simple example:

`<div id="id" class="something">coool</div>`

Becomes:

`div#id.something:coool/:`


In this example, the CHML syntax div#id.something:coool/: is translated into the equivalent HTML code `<div id="id" class="something">coool</div>`. 

## CHML vs HTML

In CHML, the div element is defined using the div keyword, the id attribute is defined using the #id syntax, and the class attribute is defined using the .something syntax. The content of the element is defined between the : and /: delimiters. 

In HTML, the div element is defined using the `<div>` and `</div>` tags, the id attribute is defined using the id attribute, and the class attribute is defined using the class attribute. The content of the element is defined between the opening and closing tags.


### A Nested Example:

div#id.something:coool/:

`<p id="someID" class="aClass">This is <em id="leId">Emphasize</em> Text</p>`

 becomes 
 
 `p#someId.aClass:This is :em#leID:Emphasize /: Text/:`
 
 

## A complex example:

```
div#main-container.container:
  h1#heading.primary-heading:Welcome to our website/:
  p#intro-text.lead:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    :em#important-note:Please note that all information on this website is for educational purposes only and should not be used as a substitute for professional advice./:
  div#content.row:
    div#left-column.column:
      h2#services-heading:Our Services/:
      ul#services-list:
        li#service-1:Service 1/:
        li#service-2:Service 2/:
        li#service-3:Service 3/:
    div#right-column.column:
      h2#contact-heading:Contact Us/:
      p#contact-details:
        Contact us at:
        :br:
        email: info@ourwebsite.com
        :br:
        phone: 555-555-5555
        :br:
        address: 123 Main Street, Anytown, USA
  div#footer.footer:
    p#copyright:Copyright 2022 Our Website/:
/:
```

