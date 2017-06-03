This is a quick python hack to get Los Angeles weather from https://openweathermap.org/current. The script
uses the pyowm wrapper library to simplify openweathermap's API and to satisfy minimum requirements in 
a hurry.

To run the script you will need Python 2.7 and the pip Python package management system installed on your system.
As systems vary widely from Windows, Unix and Linux please consult the documentation for your OS as to the particulars
of installation.

To find out which  version of Python you have; from the command line type "python --version". 
Assuming you have the correct version of Python add that you have pip run the following command:

pip install pyowm

Assuming all went well with the install of Python and pyowm you should be able to run the script as follows:

./owm_weather.py

NOTES on use:

1. OpenWeatherMap requires an account be set up and that you acquire an API key to use their service, I have all ready
done so and hardcoded my key into the code. I'm not sure what overall restrictions they place on the key usage regardingnumber of site hits and/or computers.

2. The timestamp is in GMT ; GMT is PST plus 8 hours.
