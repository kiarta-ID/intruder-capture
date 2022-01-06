<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        figure {
            display: inline-block;
        }
    </style>
    <link rel="{{ asset('/bootstrap/css/bootstrap.min.css') }}">
</head>

<body>
    {{ $images->links('vendor.pagination.bootstrap-4') }}

    @foreach($images as $image)
    <figure>
        <img src="/storage/{{ $image->image_url }}" width="200px">
        <figcaption>{{ $image->created_at }}</figcaption>
    </figure>
    @endforeach
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
    <script src="{{ asset('/bootstrap/js/bootstrap.min.js') }}"></script>
</body>

</html>