DecodeValidateCode
==================

An simple example in python to show how to decode validate code.

# The basic case
![the simplest case](docs/images/1529.jpeg)

As you seen it's a simplest case which contains four decimals.

The solution can be described to three steps: *binary*, *devide*, *recognize*.
## 0)Prepare types
This is a preparation step, so we called it step Zero. In this step we need to make all of possible occurs character to be a seperated image file.
![0](docs/images/0.jpg)
![1](docs/images/1.jpg)
![2](docs/images/2.jpg)
![3](docs/images/3.jpg)
![4](docs/images/4.jpg)
![5](docs/images/5.jpg)
![6](docs/images/6.jpg)
![7](docs/images/7.jpg)
![8](docs/images/8.jpg)
![9](docs/images/9.jpg)
## 1)Binary
In this step we will transform the origin image into a black and white image. The theory is the color is consist of RGB three basic colors, so we can set a global threshold to do the binary operation. 
## 2)Devide
In this step we will split the image into four parts, each part contains a decimal.
## 3)Recognize
In this step we wiil take each piece of our four parts to compare to the types we made in step zero and find the most similar one, and then we will know what character it is. After we done four parts we just need to join the four characters into one word and we got the anser.