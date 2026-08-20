# Blade Inspired Template Engine

wip

## Derivatives

### @include

`index.html`:

```html
<html>
<head>
    <title>Include Derivative</title>
</head>

<body>
    @include(header.html)
</body>
</html>
```

`header.html`:

```html
<header>
    <nav>
        <a href="#">Home</a>
        <a href="#">Links</a>
        <a href="#">Blogs</a>
    </nav>
</header>
```