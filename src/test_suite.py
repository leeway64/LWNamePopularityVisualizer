from HashSet import HashSet


class TestSuite:
    def test_add_remove_size(self):
        set1 = HashSet(5000)
        assert set1.size() == 0

        set1.add(101)
        assert set1.size() == 1
        set1.remove(101)
        assert set1.empty() == True
        assert set1.size() == 0

        set1.add(1,2,3,4)
        assert set1.size() == 4
        set1.remove(2)
        assert set1.size() == 3

    def test_contains_equals(self):
        set1 = HashSet(120)
        set2 = HashSet(240)

        assert not set1.contains(456)
        assert not set2.contains(7894231)
        assert set1 == set2

        set1.add(1)
        set1.add(2)
        set1.add(4)
        set1.add(8)
        set1.add(16)
        assert set1.contains(16)

        set2.add(1)
        set2.add(2)
        set2.add(4)
        set2.add(8)
        set2.add(16)
        assert set1 == set2
        set2.add(32)
        assert set1 != set2
        assert set2.contains(32)
        assert set2.contains(64) == False
    
    def test_strings(self):
        set1 = HashSet(800)
        
        set1.add("a")
        set1.add("b")
        set1.add("c")
        set1.add("a")
        assert set1.size() == 3  # No duplicates are allowed
        assert set1.contains("c")

        set1.remove("b")
        assert set1.contains("b") != True
