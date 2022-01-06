<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ImageController;
use PhpParser\Builder\Class_;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});
Route::get('/up', function () {
    return view('upImage');
})->name('image.index');

Route::post('/up', [ImageController::class, 'store'])->name('image.store');

Route::get('/image', [ImageController::class, 'index'])->name('image.index');