library(shiny)
library(shinythemes)
library(DT)
library(readr)
library(dplyr)
library(reticulate)
#use_python("/usr/local/bin/python3")
#Loads Python Shell
#repl_python()
#source('~/Independent_Study/IS_Analytics/data_prep_shiny.R')
#source('~/Independent_Study/IS_Analytics/synergy_data.R')

ui <- navbarPage(
  theme = shinytheme("yeti"),
  p("Milwaukee Bucks - Research and Innovation")
  ,    
  
  tabPanel("Home", 
           fluidPage(tags$img(src = "Milwaukee_Bucks.png", height = 200, width = 200, align = "center"),
                      tags$img(src = "Milwaukee_Bucks.png", height = 200, width = 200, align = "right"),
                      
                    
            headerPanel(
              h1(strong("Milwaukee Bucks Research and Innovation Interview Project",style = "font-family: 'Oswald'; font-si8pt"), align = "center")
              
            ),
            
            
            
            headerPanel(
              h3(strong("Welcome to Christien Wright's Research and Innovation project!",style = "font-family: 'Oswald'; font-si12pt"), align = "center")
              
              ),
            
            headerPanel(
              h3("Thank you for taking the time to view this project.",style = "font-family: 'Oswald'; font-si12pt", align = "center")
              
            ),
            
            headerPanel(
              h3("To view responses, please select the 'Project' tab at the top next to the home tab.", style = "font-family: 'Oswald'; font-si12pt", align = "center")
           ),
            
            headerPanel(
              h3("The 'Appendix' tab will lead you to the completed pdf, along with code.",style = "font-family: 'Oswald'; font-si12pt", align = "center")
              
              ),
            headerPanel(h3('If you have time, you can watch my presentation of injury data analysis at the NYC Media Lab Virtual Summit, which will tie into this project.',style = "font-family: 'Oswald'; font-si12pt", align = 'center',
                           br(), br(),
                p(tags$iframe(width=1000, height=615, src="https://www.youtube.com/embed/SK4A5wxJgjc", 
                              frameborder="0", allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture", 
                              allowfullscreen=NA, align = 'center')
                  )
              )
            )
           
           ,
           
             mainPanel(
               
               
              
               
               br(),
               br(),
               br(),
               
               p("Go Bucks!", style = "font-family: 'Oswald'; font-si16pt"),
               
               br(),
               
               tags$img(src = "wright.jpg", height = 200, width = 150),
               
               br(),
               
               br(),
               
               p("Christien Wright", style = "font-family: 'Oswald'; font-si16pt"),
               
               p("Director of Analytics, University of Memphis Men's Basketball", style = "font-family: 'Oswald'; font-si16pt"),
               
               p("UMass Amherst '20", style = "font-family: 'Oswald'; font-si16pt"),
               
               p("MBA/MS Sport Management", style = "font-family: 'Oswald'; font-si16pt"),
               
               p("Amherst College '18", style = "font-family: 'Oswald'; font-si16pt"),
               
               p("BA Statistics", style = "font-family: 'Oswald'; font-si16pt")
              
             
               
             
          )
             
)
)
  ,
  
  navbarMenu(
    "Project",
    tabPanel("Question One",
             fluidPage(
               headerPanel(
               
              h4(strong("Extract and clean data from a publicly available dataset (limit 1000 records/rows).  
               From this data, build an analytically based argument.  
               Please include appropriate data visualizations.  
               Limit text and visualizations to 2 pages in PDF format.  
               Use your software or language of choice.  
               Please provide the code, workbook, or link to your work.  
               Note that the any code/work will not count to your two-page maximum.", style = "font-family: 'Oswald'; font-si24pt")
                 , align = 'center')),
              
               tableOutput("to"),
               tableOutput("td"),
               tableOutput("po"),
               tableOutput("pd")
               
             )
    ),
    
    tabPanel("Question Two",
             fluidPage(
               headerPanel(
                 h4(strong("Who is currently the most undervalued player in the NBA?", style = "font-family: 'Oswald'; font-si20pt"), align = 'center')),
               
               DTOutput("summary_lineup"),
               
               DTOutput("post_game_Amherst"),
               
               
               DTOutput("post_game_Opponent")
               
               
             )
    ),
    
    tabPanel("Question Three",
             fluidPage(img(src = "memphis_tigers_logo.png", height = 200, width = 200, align = "left"),
                       img(src = "Milwaukee_Bucks.png", height = 200, width = 200, align = "right"),
                       headerPanel(h3(strong("What separates you from the other applicants for these positions?", style = "font-family: 'Oswald'; font-si20pt"), align = 'center'))
  
             ,
               headerPanel(
                 h4("I’ve had the unique opportunity to develop an analytics department for the University of Memphis working with assistant coach Cody Toppert, who previously coached with the Phoenix Suns and was the head coach of the NAZ Suns. 
                  We’ve developed the most advanced (and robust) analytics system in college basketball - coaching analytics, player evaluation and development, and recruiting. 
                  This led to consulting - supporting other colleges, NBA coaches and players with analytical reporting, specifically coaching strategy and player development plans. 
                  My academic background, coaching/playing career, and work experience has cultivated a unique perspective.",style = "font-family: 'Oswald'; font-si20pt", align = 'center'))
               ,
               
               img(src = "pregame.png", height = 850, width = 650, align = "left"),
             br(), br(),
               img(src = "memphis.jpg", height = 850, width = 550, align = "center"),
               
             img(src = "precious.png", height = 850, width = 650, align = "right"))
             
    )
             
    
    
    
  ),
  
  
  navbarMenu(
    "Appendix",
    tabPanel("Code")
  )
  


)









server <- function(input, output){
  
    
  
  
  output$team_rankings_offense <- renderDT(team_leaders_offense_d3)
  
  output$team_rankings_defense <- renderDT(team_leaders_defense_d3)
  
  output$post_game_Amherst <- renderDT(post_game_Amherst) 
  
  output$post_game_Opponent <- renderDT(post_game_Opponent) 
  
  output$summary_lineup <- renderDT(summary_lineup) 
  
  
  output$to <- renderTable(to)
  
  output$td <- renderTable(td)
  
  output$po <- renderTable(po)
  
  output$pd <- renderTable(pd)
  
  

}

shinyApp(ui, server)


