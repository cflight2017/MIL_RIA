# Milwaukee Bucks - Research and Innovation Analyst Position

# Question One

# Data Description
I collected draft combine data from nba.com and then joined it with career statistics from basketball reference. I performed a left join to make sure that all players in the dataset were in the combine and drafted also. I handled the missing data from the combine by removing missing values, there was a lot of missing data for the combine measurements because the dataset only includes players who went to the combine and players who were subsequently drafted. Most players who go undrafted typically don't last very long in the NBA, thus I didn't feel compelled to include them, even if they were invited and participated in the combine. Also, with some top prospects choosing not to participate, there's a lot of prospects who were drafted who are not included because they didn't participate in the combine, thus there isn't combine data available for them. To solve this issue, I simply imputed data via MissForest to reconcile data for the model building. This will facilitate a more representative size given this data spans from 2000 to 2018.


### Note: There are a mix of r and python files, but ultimately this experience is best consumed via the shiny app.

### Question two - in Python
