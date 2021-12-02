#include <gtest/gtest.h>
#include <calculator.h>

// Demonstrate some basic assertions.
TEST(HelloTest, BasicAssertions) {
   Calculator cal;
   EXPECT_EQ(cal.sum(2,3),5);
}