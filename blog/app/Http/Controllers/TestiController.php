<?php

namespace App\Http\Controllers;

use Jessengers\Mongodb\Eloquent\Model as Eloquent;
use Illuminate\Http\Request;
use \App\User;

class TestiController extends Controller
{
    public function index(){
        $data = User::all();

        return view('welcome', compact('data'));

        
    }
}