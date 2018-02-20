
// MOCK_REGISTER_WITHOUT_FIELDS (A mock 64-bit register with no fields)
// Register does not belong to the aarch64 architecture
namespace mock_register_without_fields
{
	inline uint64_t get(void) noexcept { GET_SYSREG_FUNC(mock_register_without_fields) }
	inline void set(uint64_t val) noexcept { SET_SYSREG_BY_VALUE_FUNC(mock_register_without_fields, val) }
}
