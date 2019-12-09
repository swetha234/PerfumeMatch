<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Laravel</title>

        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Nunito:200,600" rel="stylesheet">
        <link rel="stylesheet" href="{{ URL::asset('css/styles.css') }}">
       
    </head>
    <body>
        <div class="flex-center position-ref full-height",, id="backgroundimage">
            @if (Route::has('login'))
                <div class="top-right links">
                    @auth
                        <a href="{{ url('/home') }}">Home</a>
                    @else
                        <a href="{{ route('login') }}">Login</a>

                        @if (Route::has('register'))
                            <a href="{{ route('register') }}">Register</a>
                        @endif
                    @endauth
                </div>
            @endif

            <div class="content">
            <div class="content" >
                <div class="title m-b-md">  PerfumeMatch </div>
                <form class="" action="{{URL::to('/store')}}" method="post">
                <label style="color: black; "><b>Name:</b></label>
     <input type="text"   name=" name" placeholder="Enter name" value=" "> 
                    <br><br>
                    <label style="color: black;"><b>Email:</b></label>
                  <input type="text" name="email" placeholder="Enter email" value=" ">
                    <br><br>
                    <label style="color: black;"><b>Password:</b></label>
                    <input type="password" name="password" placeholder="Enter password" value=" ">
                    <br><br>
                    <input type="hidden" name="_token" value="{{csrf_token()}}">
                    <br>
                    <button type="submit" name="button"> SignUp</button>
</form>


            </div>
            
            {{ $data }} 
                
            </div>
        </div>
    </body>
</html>
