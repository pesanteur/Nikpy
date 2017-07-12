nikpy/data_util.py|31 col 6| #TODO: have this build json file without deleting previous file. Possibly use log to improve
nikpy/data_util.py|55 col 6| #TODO: This does not perfectly pull information table from site.
nikpy/data_util.py|57 col 6| #TODO: Add pandas pd.read_html() to this to make this easier to use
nikpy/data_util.py|67 col 80| car_table = table[3] # Much faster and easier way of reading table data // TODO: change entire program to be able to use this
nikpy/login_util.py|13 col 6| #TODO: use Selenium specific sleep function that works on page load.
nikpy/navi_util.py|5 col 6| #TODO: Switch back to click
nikpy/nikpy.py|44 col 10| #TODO: Include start and end date range in date range util
nikpy/nikpy.py|66 col 10| #TODO: Make this more pythonic. Test context manager.
nikpy/nikpy.py|128 col 10| #TODO: Expand on this function
nikpy/nikpy.py|139 col 11| # TODO: break down get pic urls into multiple functions so we can pull further
nikpy/nikpy.py|150 col 7| # TODO: Create function that pulls invoicing information by code
nikpy/nikpy.py|158 col 28| chassis_no = None #TODO: Get last four digits of Chassis No. from somewhere above!
nikpy/pic_pull.py|8 col 6| #TODO: Break this down into a smaller function to make it more readable
nikpy/pic_pull.py|25 col 46| print('Table not uploaded') #TODO: Start pulling tables here. How to make pull happen with viewing below...maybe remove other else statement?
nikpy/pic_pull.py|28 col 49| # This breaks main code somehow TODO: Fix this later
nikpy/pic_pull.py|49 col 14| #TODO: remove the following when above found to work
run.py|8 col 23| script, date = argv # TODO: In future use argparse and be explicit with what date format is. (Year/Month/Day)
runp.py|8 col 23| script, code = argv # TODO: In future use argparse and be explicit with what date format is. (Year/Month/Day)
test_grab.py|13 col 7| # TODO: Build these links into a list/dictionary/json file. Then scrape with a tool like scrapy to speed up the process
test_grab.py|23 col 7| # TODO: to pull code from this url
test_grab.py|27 col 3| # TODO: Iterate through list and download image using requests
test_grab.py|30 col 88| image_file = open(os.path.join('nik_pictures', os.path.basename(picture)), 'wb') # TODO: Regex is too much work just use split
