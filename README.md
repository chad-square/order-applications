# OrderApplications.py
A python script that uses wmctrl to order your running applications to the workspace of your choosing.

## Usage

```bash
# Install wmctrl
sudo apt install wmctrl

#  Run 
wmctrl -l -x 
# In the result of the above command, the third column will contain the application name
# Use the above-mentioned application name, up until but not including the dot (.)

# Update the get_application_window_index method to include a case for the application name and the index of window you want it to appear on
get_application_window_index()
```
