library(gvegayon/rgexf)

if ( interactif ())  {

path  <-  system.file ( "LastGraph.gexf" ,  package = "rgexf" ) 
graph  <-  read.gexf ( path ) 
plot ( graph )

}