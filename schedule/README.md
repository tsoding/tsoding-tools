# Stream Scheduler #

## Usage ##

From the root of the tools

```console
$ ./venv/bin/ipython
> from schedule import schedule
> schedule(recipe_filepath='./schedule/recipe.yaml')
```

Import `schedule.csv` to the Google Calendar

## Import to Google Calendar ##

https://support.google.com/calendar/answer/37118?hl=en

- Open Google Calendar on a computer. Note: You can only import from a computer, not a phone or tablet.
- In the top right, click Settings
- Open the Calendars tab.
- Click Import calendar between the "My calendars" and "Other Calendars" sections.
- Click Choose File and select the file you exported. The file should end in "ics" or "csv"
- Choose which calendar to add the imported events to. By default, events will be imported into your primary calendar.
- Click Import.
