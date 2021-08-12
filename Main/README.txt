To start the scraping scripts, use the execute_main.py file

After scraping, you'll have to manually update the new data to the working sheet (which is Group 9 CAT Final Project)

- When using update button on STI ETF sheet, select the basket-sg file in the basket folder.

- For the update button on SiMSCI sheet, select the SG-Stocks.xlsx in the scraper folder

Since no live data can be collected without Bloomberg Plugins, we have made a separate static work sheet within the excel files
There are 2 ways you can interact with this trading platform: manually or have it done automatically

- Manual: With the built-in buttons, you can enter or exit position. The indicator at the top row, which will change to "True" when the position is good to enter or exit will help you make the decision. You can enter multiple position at once.

- Automatic: Using the indicator, the scripts will automatically know when to enter/exit. However, it can only enter one positionat a time.
