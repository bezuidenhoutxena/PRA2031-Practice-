class Spring:
    """A class representing a spring following Hooke's law."""
    
    # Your merged implementation here
    pass

# Test your implementation
spring = Spring(k=100, rest_length=0.5)  # 100 N/m, 0.5 m rest length
print(f"Force at 0.1m displacement: {spring.force(0.1)} N")
# Expected: -10.0 N (restoring force)