# About this `/docs` directory

The contents of this directory are deployed via GitHub Pages as [http://phenopackets.org](http://phenopackets.org).

The CNAME file determines which site can legitimately redirect here.
Currently, this is http://phenopackets.org. The CNAME in the master branch of
this repo must correspond for the site to be viewable as GitHub pages.

## Deployment structure

Although the website appears seamless to a user, from an author's point of view
there are two types of content, HTML and Markdown. These are divided into two
directories, respectively: `/site` and `/content`. The goal behind this
distinction is to encourage authors to improve and create content in Markdown,
which is visible both through the fancy portal, as well as through the GitHub
developer interface.

### `index.html`

The file `index.html` defines a basic marketing-style landing page with high-level content about PhenoPackets and several links to other aspects of the project, including the other PhenoPackets repositories. In addition, index.html has JavaScript that dynamically loads more detailed information from Markdown files, and optionally renders these Markdown files (if the user clicks the 'Details' buttons on the page).

### Markdown content

The directory `/content` contains several Markdown files that serve two purposes:

- These files may be viewed directly via GitHub, providing a source of reusable documentation
- The content of these files may be more easily edited than HTML


## Editing and Adding Content

The high-level content is within `index.html` and the detailed content is within the Markdown files in `/content`.

### Editing index.html

Please use two-column indentation and no tab stops. HTML is difficult to maintain if indentation is not uniform.

Please test any changes on both narrow and wide screens. Ideally, use your browser's 'Responsive Design Mode' to allow you to see how the site looks on a mobile device.


## Editing Markdown files

It is important to realize that the same markdown files are rendered through the http://phenopackets.org site as well as through the GitHub portal. Relative image links from Markdown files in `/content' to image files in `/content` need to be specified with a relative prefix `![](./` as in the example below:

```
![](./phenopacket-ecosystem_2016-02-18a.png)
```

When the `index.html` page dynamically loads the Markdown content, the JavaScript code will *adjust* the prefix above to be `![](content/`so that the page can refer to the image file relative to index.html; it's a hack, but it works as long as Markdown authors use the above convention.


## Local Testing

It is necessary to run a local HTTP server to be able to try out the website effectively. I recommend `http-server`, which is easy to install and use if you already have a NodeJS environment:

```
npm install -g http-server
```

Once you have an HTTP server, it should be started so that it serves the `phenopacket-format/docs` directory as the website base URL `/`. In addition, caching should be disabled, so that local edits can be seen upon page refresh. For example, here is how to do this with `http-server`:


```
cd phenopacket-format/docs/
http-server -c-1 .
```


### Credits

- https://commons.wikimedia.org/wiki/File:DNA_com_GGN.jpg
- [Start Bootstrap](http://startbootstrap.com/)
- [Stylish Portfolio](http://startbootstrap.com/template-overviews/stylish-portfolio/)
