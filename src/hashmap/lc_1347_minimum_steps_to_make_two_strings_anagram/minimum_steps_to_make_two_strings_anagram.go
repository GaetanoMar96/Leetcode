func minSteps(s string, t string) int {
    charMaps := make(map[rune]int)
    for _, char := range s {
        charMaps[char]++
    }
    for _, char := range t {
        if count, ok := charMaps[char]; ok && count > 0 {
            charMaps[char]--
        }
    }
    steps := 0
    for _, count := range charMaps {
        steps += count
    }
    return steps
}