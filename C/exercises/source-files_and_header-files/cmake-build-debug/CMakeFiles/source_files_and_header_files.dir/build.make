# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.8

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/kaspar/DAT113/exercises/source-files_and_header-files

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/kaspar/DAT113/exercises/source-files_and_header-files/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/source_files_and_header_files.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/source_files_and_header_files.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/source_files_and_header_files.dir/flags.make

CMakeFiles/source_files_and_header_files.dir/main.c.o: CMakeFiles/source_files_and_header_files.dir/flags.make
CMakeFiles/source_files_and_header_files.dir/main.c.o: ../main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/kaspar/DAT113/exercises/source-files_and_header-files/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/source_files_and_header_files.dir/main.c.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/source_files_and_header_files.dir/main.c.o   -c /Users/kaspar/DAT113/exercises/source-files_and_header-files/main.c

CMakeFiles/source_files_and_header_files.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/source_files_and_header_files.dir/main.c.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kaspar/DAT113/exercises/source-files_and_header-files/main.c > CMakeFiles/source_files_and_header_files.dir/main.c.i

CMakeFiles/source_files_and_header_files.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/source_files_and_header_files.dir/main.c.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kaspar/DAT113/exercises/source-files_and_header-files/main.c -o CMakeFiles/source_files_and_header_files.dir/main.c.s

CMakeFiles/source_files_and_header_files.dir/main.c.o.requires:

.PHONY : CMakeFiles/source_files_and_header_files.dir/main.c.o.requires

CMakeFiles/source_files_and_header_files.dir/main.c.o.provides: CMakeFiles/source_files_and_header_files.dir/main.c.o.requires
	$(MAKE) -f CMakeFiles/source_files_and_header_files.dir/build.make CMakeFiles/source_files_and_header_files.dir/main.c.o.provides.build
.PHONY : CMakeFiles/source_files_and_header_files.dir/main.c.o.provides

CMakeFiles/source_files_and_header_files.dir/main.c.o.provides.build: CMakeFiles/source_files_and_header_files.dir/main.c.o


CMakeFiles/source_files_and_header_files.dir/student.c.o: CMakeFiles/source_files_and_header_files.dir/flags.make
CMakeFiles/source_files_and_header_files.dir/student.c.o: ../student.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/kaspar/DAT113/exercises/source-files_and_header-files/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object CMakeFiles/source_files_and_header_files.dir/student.c.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/source_files_and_header_files.dir/student.c.o   -c /Users/kaspar/DAT113/exercises/source-files_and_header-files/student.c

CMakeFiles/source_files_and_header_files.dir/student.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/source_files_and_header_files.dir/student.c.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kaspar/DAT113/exercises/source-files_and_header-files/student.c > CMakeFiles/source_files_and_header_files.dir/student.c.i

CMakeFiles/source_files_and_header_files.dir/student.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/source_files_and_header_files.dir/student.c.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kaspar/DAT113/exercises/source-files_and_header-files/student.c -o CMakeFiles/source_files_and_header_files.dir/student.c.s

CMakeFiles/source_files_and_header_files.dir/student.c.o.requires:

.PHONY : CMakeFiles/source_files_and_header_files.dir/student.c.o.requires

CMakeFiles/source_files_and_header_files.dir/student.c.o.provides: CMakeFiles/source_files_and_header_files.dir/student.c.o.requires
	$(MAKE) -f CMakeFiles/source_files_and_header_files.dir/build.make CMakeFiles/source_files_and_header_files.dir/student.c.o.provides.build
.PHONY : CMakeFiles/source_files_and_header_files.dir/student.c.o.provides

CMakeFiles/source_files_and_header_files.dir/student.c.o.provides.build: CMakeFiles/source_files_and_header_files.dir/student.c.o


# Object files for target source_files_and_header_files
source_files_and_header_files_OBJECTS = \
"CMakeFiles/source_files_and_header_files.dir/main.c.o" \
"CMakeFiles/source_files_and_header_files.dir/student.c.o"

# External object files for target source_files_and_header_files
source_files_and_header_files_EXTERNAL_OBJECTS =

source_files_and_header_files: CMakeFiles/source_files_and_header_files.dir/main.c.o
source_files_and_header_files: CMakeFiles/source_files_and_header_files.dir/student.c.o
source_files_and_header_files: CMakeFiles/source_files_and_header_files.dir/build.make
source_files_and_header_files: CMakeFiles/source_files_and_header_files.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/kaspar/DAT113/exercises/source-files_and_header-files/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking C executable source_files_and_header_files"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/source_files_and_header_files.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/source_files_and_header_files.dir/build: source_files_and_header_files

.PHONY : CMakeFiles/source_files_and_header_files.dir/build

CMakeFiles/source_files_and_header_files.dir/requires: CMakeFiles/source_files_and_header_files.dir/main.c.o.requires
CMakeFiles/source_files_and_header_files.dir/requires: CMakeFiles/source_files_and_header_files.dir/student.c.o.requires

.PHONY : CMakeFiles/source_files_and_header_files.dir/requires

CMakeFiles/source_files_and_header_files.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/source_files_and_header_files.dir/cmake_clean.cmake
.PHONY : CMakeFiles/source_files_and_header_files.dir/clean

CMakeFiles/source_files_and_header_files.dir/depend:
	cd /Users/kaspar/DAT113/exercises/source-files_and_header-files/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/kaspar/DAT113/exercises/source-files_and_header-files /Users/kaspar/DAT113/exercises/source-files_and_header-files /Users/kaspar/DAT113/exercises/source-files_and_header-files/cmake-build-debug /Users/kaspar/DAT113/exercises/source-files_and_header-files/cmake-build-debug /Users/kaspar/DAT113/exercises/source-files_and_header-files/cmake-build-debug/CMakeFiles/source_files_and_header_files.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/source_files_and_header_files.dir/depend

