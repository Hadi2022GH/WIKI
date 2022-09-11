# Django

**Django** (/ˈdʒæŋɡoʊ/ JANG-goh; sometimes stylized as django) is a free and open-source, [Python](/wiki/Python)-based web framework that that allows for the design of web 
applications that generate [HTML](/wiki/HTML) dynamically and follows the model–template–views (MTV) architectural pattern. It is maintained by the Django Software Foundation (DSF), an independent organization established in the US as a 501(c)(3) non-profit.

Django's primary goal is to ease the creation of complex, database-driven websites. The framework emphasizes reusability and "pluggability" of components, less code, low coupling, rapid development, and the principle of don't repeat yourself.[Python](/wiki/Python) is used throughout, even for settings, files, and data models. Django also provides an optional administrative create, read, update and delete interface that is generated dynamically through introspection and configured via admin models.

Some well-known sites that use Django include Instagram, Mozilla, Disqus, Bitbucket, Nextdoor and Clubhouse.

#### Components ####

Screenshot of the Django admin interface for modifying a user account
Despite having its own nomenclature, such as naming the callable objects generating the [HTML](/wiki/HTML) responses "views", the core Django framework can be seen as an MVC architecture. It consists of an object-relational mapper (ORM) that mediates between data models (defined as [Python](/wiki/Python) classes) and a relational database ("Model"), a system for processing [HTML](/wiki/HTML) requests with a web templating system ("View"), and a regular-expression-based URL dispatcher ("Controller").

Also included in the core framework are:

* a lightweight and standalone web server for development and testing
* a form serialization and validation system that can translate between HTML forms and values suitable for storage in the database
* a template system that utilizes the concept of inheritance borrowed from object-oriented programming
* a caching framework that can use any of several cache methods
* support for middleware classes that can intervene at various stages of request processing and carry out custom functions
* an internal dispatcher system that allows components of an application to communicate events to each other via pre-defined signals
* an internationalization system, including translations of Django's own components into a variety of languages
* a serialization system that can produce and read XML and/or JSON representations of Django model instances
* a system for extending the capabilities of the template engine
an interface to Python's built-in unit test framework
