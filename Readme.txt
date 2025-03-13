{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Bold;\f1\froman\fcharset0 Times-Roman;\f2\fmodern\fcharset0 Courier;
\f3\froman\fcharset0 Times-Italic;\f4\fmodern\fcharset0 Courier-Bold;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red0\green0\blue233;\red109\green109\blue109;
}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c0\c0\c93333;\cssrgb\c50196\c50196\c50196;
}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid1\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{circle\}}{\leveltext\leveltemplateid2\'01\uc0\u9702 ;}{\levelnumbers;}\fi-360\li1440\lin1440 }{\listname ;}\listid1}
{\list\listtemplateid2\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid101\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid2}
{\list\listtemplateid3\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid201\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid3}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}{\listoverride\listid2\listoverridecount0\ls2}{\listoverride\listid3\listoverridecount0\ls3}}
\paperw11900\paperh16840\margl1440\margr1440\vieww18860\viewh18360\viewkind0
\deftab720
\pard\pardeftab720\sa280\partightenfactor0

\f0\b\fs36 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Instructions for Running the Colab Notebook & Streamlit NDVI Analysis App
\fs28 \
\pard\pardeftab720\sa298\partightenfactor0

\fs36 \cf0 - Running the Colab Notebook\
\pard\pardeftab720\partightenfactor0

\fs28 \cf0 Google Earth Engine (GEE) Authentication\
\

\f1\b0\fs24 Before running the notebook, authenticate your Google Earth Engine (GEE) account:\
\pard\pardeftab720\partightenfactor0

\f2\fs26 \cf0 ee.Authenticate()\
ee.Initialize()\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls1\ilvl0
\f0\b\fs24 \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Use the following credentials to log in and run the Colab file:
\f1\b0 \
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\partightenfactor0
\ls1\ilvl1
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Email ID:
\f1\b0  {\field{\*\fldinst{HYPERLINK "mailto:t9561568@gmail.com"}}{\fldrslt \cf3 \ul \ulc3 \strokec3 t9561568@gmail.com}}\
\ls1\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Password:
\f1\b0  test9876\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls1\ilvl0
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 After running the notebook in Colab
\f1\b0 , you will see a prompt: 
\f3\i \'93Allow this notebook to access your Google credentials?\'94
\f1\i0  \uc0\u8594  Click 
\f0\b Allow
\f1\b0  to proceed.\cf4 \strokec4 \
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf0 \strokec2 - Running the Streamlit NDVI Analysis App\
\pard\pardeftab720\sa280\partightenfactor0

\fs28 \cf0 1. Requirements\
\pard\pardeftab720\sa240\partightenfactor0

\f1\b0\fs24 \cf0 Before running the application, ensure the following dependencies are installed:\
\pard\pardeftab720\sa319\partightenfactor0

\f0\b \cf0 \strokec2 Dependencies:\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls2\ilvl0
\f1\b0 \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Python 3.9+\
\ls2\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Streamlit\
\ls2\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Google Earth Engine (GEE)\
\ls2\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 GeoPandas\
\ls2\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Geemap\
\ls2\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 NumPy\
\ls2\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Matplotlib\
\ls2\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Seaborn\
\ls2\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Plotly\
\pard\tx720\pardeftab720\partightenfactor0
\cf0 \
\pard\pardeftab720\sa319\partightenfactor0

\f0\b \cf0 Install Dependencies:\
\pard\pardeftab720\sa240\partightenfactor0

\f1\b0 \cf0 \strokec2 Run the following commands to install the required Python libraries:\
\pard\pardeftab720\partightenfactor0

\f2\fs26 \cf0 !pip install geemap geopandas matplotlib numpy seaborn streamlit plotly\
\pard\pardeftab720\partightenfactor0

\f1\fs24 \cf4 \strokec4 \
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs28 \cf0 \strokec2 2. Running the Application Locally
\fs36 \
\pard\pardeftab720\sa240\partightenfactor0

\f1\b0\fs24 \cf0 To launch the 
\f0\b Streamlit web app
\f1\b0 , navigate to the directory containing the script and run:\
\pard\pardeftab720\partightenfactor0

\f2\fs26 \cf0 streamlit run project.py\
\
\pard\pardeftab720\sa240\partightenfactor0

\f1\fs24 \cf0 This will start a 
\f0\b local server
\f1\b0 , and you will see an output like:\
\pard\pardeftab720\partightenfactor0

\f2\fs26 \cf0 You can now view your Streamlit app in your browser.\
Local URL: http://localhost:8501\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls3\ilvl0
\f0\b\fs24 \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 \
\ls3\ilvl0\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Open the Local URL (
\f4\fs26 http://localhost:8501
\f0\fs24 ) in your browser
\f1\b0  to access the interactive NDVI dashboard.\
\pard\pardeftab720\partightenfactor0
\cf4 \strokec4 \
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf0 \strokec2 Key Features of the App\
\pard\pardeftab720\sa240\partightenfactor0

\fs24 \cf0 NDVI Change Detection Maps
\f1\b0  \uc0\u8594  Visualize NDVI trends between 2016 and 2023.\u8232 
\f0\b Histogram of NDVI Changes
\f1\b0  \uc0\u8594  Interactive distribution of vegetation changes.\u8232 
\f0\b Time-Series Analysis
\f1\b0  \uc0\u8594  Line chart of mean NDVI trends.\u8232 
\f0\b Box Plot Comparison
\f1\b0  \uc0\u8594  NDVI differences between both years.\u8232 
\f0\b Dynamic Interactive Dashboard
\f1\b0  \uc0\u8594  Developed using 
\f0\b Streamlit & Plotly
\f1\b0  for an enhanced user experience.\
}
