
// MOCK_REGISTER_MULTIPLE_FIELDSETS (A mock 64-bit register with multiple fields)
// Register does not belong to the aarch64 architecture
namespace mock_register_multiple_fieldsets
{
	inline uint64_t get(void) noexcept { GET_SYSREG_FUNC(mock_register_multiple_fieldsets) }
	inline void set(uint64_t val) noexcept { SET_SYSREG_BY_VALUE_FUNC(mock_register_multiple_fieldsets, val) }

	// Fieldset valid when: the condition under which this fieldset is used
	namespace fieldset_1
	{
		namespace msb
		{
			inline uint64_t is_enabled() noexcept { IS_SYSREG_BIT_ENABLED_FUNC(mock_register_multiple_fieldsets, 63) }
			inline uint64_t is_enabled(uint64_t mock_register_multiple_fieldsets_val) noexcept { IS_BIT_ENABLED_FUNC(mock_register_multiple_fieldsets_val, 63) }
			inline uint64_t is_disabled() noexcept { IS_SYSREG_BIT_DISABLED_FUNC(mock_register_multiple_fieldsets, 63) }
			inline uint64_t is_disabled(uint64_t mock_register_multiple_fieldsets_val) noexcept { IS_BIT_DISABLED_FUNC(mock_register_multiple_fieldsets_val, 63) }
			inline void enable() noexcept { SET_SYSREG_BITS_BY_MASK_FUNC(mock_register_multiple_fieldsets, 0x8000000000000000) }
			inline uint64_t enable(uint64_t mock_register_multiple_fieldsets_val) noexcept { SET_BITS_BY_MASK_FUNC(mock_register_multiple_fieldsets_val, 0x8000000000000000) }
			inline void disable() noexcept { CLEAR_SYSREG_BITS_BY_MASK_FUNC(mock_register_multiple_fieldsets, 0x8000000000000000) }
			inline uint64_t disable(uint64_t mock_register_multiple_fieldsets_val) noexcept { CLEAR_BITS_BY_MASK_FUNC(mock_register_multiple_fieldsets_val, 0x8000000000000000) }
		}

		namespace not_msb_lsb
		{
			inline uint64_t get() noexcept { GET_SYSREG_FIELD_FUNC(mock_register_multiple_fieldsets, 0x7ffffffffffffffe, 1) }
			inline uint64_t get(uint64_t mock_register_multiple_fieldsets_val) noexcept { GET_BITFIELD_FUNC(mock_register_multiple_fieldsets_val, 0x7ffffffffffffffe, 1) }
			inline void set(uint64_t value) noexcept { SET_SYSREG_BITS_BY_VALUE_FUNC(mock_register_multiple_fieldsets, value, 0x7ffffffffffffffe, 1) }
			inline uint64_t set(uint64_t mock_register_multiple_fieldsets, uint64_t value) noexcept { SET_BITS_BY_VALUE_FUNC(mock_register_multiple_fieldsets, value, 0x7ffffffffffffffe, 1) }
		}

		namespace lsb
		{
			inline uint64_t is_enabled() noexcept { IS_SYSREG_BIT_ENABLED_FUNC(mock_register_multiple_fieldsets, 0) }
			inline uint64_t is_enabled(uint64_t mock_register_multiple_fieldsets_val) noexcept { IS_BIT_ENABLED_FUNC(mock_register_multiple_fieldsets_val, 0) }
			inline uint64_t is_disabled() noexcept { IS_SYSREG_BIT_DISABLED_FUNC(mock_register_multiple_fieldsets, 0) }
			inline uint64_t is_disabled(uint64_t mock_register_multiple_fieldsets_val) noexcept { IS_BIT_DISABLED_FUNC(mock_register_multiple_fieldsets_val, 0) }
			inline void enable() noexcept { SET_SYSREG_BITS_BY_MASK_FUNC(mock_register_multiple_fieldsets, 0x1) }
			inline uint64_t enable(uint64_t mock_register_multiple_fieldsets_val) noexcept { SET_BITS_BY_MASK_FUNC(mock_register_multiple_fieldsets_val, 0x1) }
			inline void disable() noexcept { CLEAR_SYSREG_BITS_BY_MASK_FUNC(mock_register_multiple_fieldsets, 0x1) }
			inline uint64_t disable(uint64_t mock_register_multiple_fieldsets_val) noexcept { CLEAR_BITS_BY_MASK_FUNC(mock_register_multiple_fieldsets_val, 0x1) }
		}
	}

	// Fieldset valid when: the condition under which this other fieldset is used
	namespace fieldset_2
	{
		namespace upper_half
		{
			inline uint64_t get() noexcept { GET_SYSREG_FIELD_FUNC(mock_register_multiple_fieldsets, 0xffffffffffc00000, 22) }
			inline uint64_t get(uint64_t mock_register_multiple_fieldsets_val) noexcept { GET_BITFIELD_FUNC(mock_register_multiple_fieldsets_val, 0xffffffffffc00000, 22) }
			inline void set(uint64_t value) noexcept { SET_SYSREG_BITS_BY_VALUE_FUNC(mock_register_multiple_fieldsets, value, 0xffffffffffc00000, 22) }
			inline uint64_t set(uint64_t mock_register_multiple_fieldsets, uint64_t value) noexcept { SET_BITS_BY_VALUE_FUNC(mock_register_multiple_fieldsets, value, 0xffffffffffc00000, 22) }
		}

		namespace lower_half
		{
			inline uint64_t get() noexcept { GET_SYSREG_FIELD_FUNC(mock_register_multiple_fieldsets, 0x3fffff, 0) }
			inline uint64_t get(uint64_t mock_register_multiple_fieldsets_val) noexcept { GET_BITFIELD_FUNC(mock_register_multiple_fieldsets_val, 0x3fffff, 0) }
			inline void set(uint64_t value) noexcept { SET_SYSREG_BITS_BY_VALUE_FUNC(mock_register_multiple_fieldsets, value, 0x3fffff, 0) }
			inline uint64_t set(uint64_t mock_register_multiple_fieldsets, uint64_t value) noexcept { SET_BITS_BY_VALUE_FUNC(mock_register_multiple_fieldsets, value, 0x3fffff, 0) }
		}
	}
}
