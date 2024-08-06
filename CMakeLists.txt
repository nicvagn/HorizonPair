cmake_minimum_required(VERSION 3.4...3.21)

# SET'S LIST NO LONGER IGNORES EMPTY SETS
cmake_policy(SET CMP0007 NEW) 
# change relative source path's to absolute
CMAKE_POLICY(SET CMP0076 NEW)

project(HorizonPair VERSION 0.1 LANGUAGES CXX)

# set the wich standard version (C++) the target's will be compiled with.
# Make it required
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED On)
set(CMAKE_CXX_FLAGS "-Wall -Wextra -fPIC")
# set the standard version of C
set(CMAKE_C_STANDARD 23)
set(CMAKE_C_FLAGS "-Wall -Wextra -fPIC")
set(CMAKE_C_STANDARD_REQUIRED ON)

# tell CMake to run the Qt tools moc, rcc, and uic automatically
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

# dependancies
# QT modules
find_package(Qt6 COMPONENTS Core REQUIRED)
find_package(Qt6 COMPONENTS Widgets REQUIRED)
find_package(Qt6 COMPONENTS Test REQUIRED)

# add compile targets
add_executable(HorizonPair src/main.cpp)

# link the executable to the Qt modules
target_link_libraries(HorizonPair PRIVATE Qt6::Core Qt6::Widgets Qt6::Test)
