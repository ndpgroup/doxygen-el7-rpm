# Makefile for source rpm: doxygen
# $Id$
NAME := doxygen
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
